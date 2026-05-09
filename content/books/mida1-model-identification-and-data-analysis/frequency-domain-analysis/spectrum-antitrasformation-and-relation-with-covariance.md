---
book_slug: mida1-model-identification-and-data-analysis
book_title: MIDA1 Model Identification and Data Analysis
chapter_slug: frequency-domain-analysis
chapter_title: Frequency Domain Analysis
created_at: '2022-03-26T22:03:39.000000Z'
id: 121
priority: 2
slug: spectrum-antitrasformation-and-relation-with-covariance
title: Spectrum antitrasformation and relation with covariance
type: page
updated_at: '2022-03-26T22:10:42.000000Z'
---

# Spectrum antitrasformation and relation with covariance

There exists an antitrasformation:
$$\gamma_y(\tau)=\frac{1}{2\pi}\int_{-\pi}^{+\pi}{\Gamma_y(\omega)e^{j\omega\tau}d\omega}$$

Notice that the variance:
$$\gamma_y(0)=\mathbb{E}[(y(t)-m_y)^2]=\frac{1}{2\pi}\int_{-\pi}^{+\pi}{\Gamma_y(\omega)d\omega}$$
so the variance is the area below the spectrum.

There is **biunivocal relationship between spectrum and covariance function**. This means that the weak (wide sense) characterization of a process is given by the mean function and by the spectrum or the covariance function.

The spectrum and the covariance function contain the **same information under a different prospective**.