(function () {
  const root = document.documentElement.dataset.root || "";
  const input = document.getElementById("search-input");
  const results = document.getElementById("search-results");
  const wrap = document.getElementById("search-wrap");
  if (!input || !results || !wrap || typeof MiniSearch === "undefined") return;

  let index = null;
  let activeIdx = -1;
  let lastQuery = "";

  async function ensureIndex() {
    if (index) return;
    const r = await fetch(root + "search.json");
    const data = await r.json();
    index = new MiniSearch({
      idField: "id",
      fields: ["title", "book", "chapter", "body"],
      storeFields: ["url", "title", "book", "chapter", "body"],
      searchOptions: {
        boost: { title: 4, book: 2, chapter: 2 },
        prefix: true,
        fuzzy: 0.15,
        combineWith: "AND",
      },
    });
    index.addAll(data);
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function snippet(body, query) {
    if (!body) return "";
    const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    const lower = body.toLowerCase();
    let pos = -1;
    for (const t of terms) {
      const p = lower.indexOf(t);
      if (p >= 0) { pos = p; break; }
    }
    if (pos < 0) pos = 0;
    const start = Math.max(0, pos - 60);
    const end = Math.min(body.length, pos + 160);
    let s = (start > 0 ? "…" : "") + body.slice(start, end) + (end < body.length ? "…" : "");
    s = escapeHtml(s);
    for (const t of terms) {
      if (!t) continue;
      const re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi");
      s = s.replace(re, "<mark>$1</mark>");
    }
    return s;
  }

  function render(matches, query) {
    activeIdx = -1;
    if (!matches.length) {
      results.innerHTML = '<div class="search-empty">No results for “' + escapeHtml(query) + "”</div>";
      results.classList.add("open");
      return;
    }
    results.innerHTML = matches.slice(0, 10).map(function (m, i) {
      const crumb = escapeHtml(m.book) + (m.chapter ? ' <span class="sep">›</span> ' + escapeHtml(m.chapter) : "");
      return (
        '<a href="' + root + escapeHtml(m.url) + '" class="search-result" data-idx="' + i + '">' +
        '<div class="r-title">' + escapeHtml(m.title) + "</div>" +
        '<div class="r-crumb">' + crumb + "</div>" +
        '<div class="r-snippet">' + snippet(m.body, query) + "</div>" +
        "</a>"
      );
    }).join("");
    results.classList.add("open");
  }

  let timer = null;
  input.addEventListener("input", function (e) {
    clearTimeout(timer);
    const q = e.target.value.trim();
    if (!q) { results.classList.remove("open"); lastQuery = ""; return; }
    timer = setTimeout(async function () {
      await ensureIndex();
      lastQuery = q;
      const matches = index.search(q);
      render(matches, q);
    }, 80);
  });

  input.addEventListener("focus", function () {
    ensureIndex();
    if (input.value.trim()) results.classList.add("open");
  });

  document.addEventListener("click", function (e) {
    if (!wrap.contains(e.target)) results.classList.remove("open");
  });

  function items() { return results.querySelectorAll(".search-result"); }
  function setActive(i) {
    const list = items();
    list.forEach(function (el, idx) { el.classList.toggle("active", idx === i); });
    activeIdx = i;
    if (i >= 0 && list[i]) list[i].scrollIntoView({ block: "nearest" });
  }

  input.addEventListener("keydown", function (e) {
    const list = items();
    if (e.key === "ArrowDown") {
      e.preventDefault();
      if (!list.length) return;
      setActive(Math.min(list.length - 1, activeIdx + 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActive(Math.max(-1, activeIdx - 1));
    } else if (e.key === "Enter") {
      if (activeIdx >= 0 && list[activeIdx]) {
        e.preventDefault();
        window.location.href = list[activeIdx].href;
      }
    } else if (e.key === "Escape") {
      results.classList.remove("open");
      input.blur();
    }
  });

  // Cmd/Ctrl + K to focus search
  document.addEventListener("keydown", function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      input.focus();
      input.select();
    }
  });
})();
