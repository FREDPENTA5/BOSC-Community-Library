# Legal Analysis of the BOSC Community Library

## Executive Summary
This document provides a comprehensive legal and ethical rationale for the selection of the Mozilla Public License 2.0 (MPL-2.0) for the BOSC Community Library project.

## License Superiority for Public-Sector Projects
The BOSC Community Library is designed for public-sector transparency and community resilience. Traditional permissive licenses (like MIT or Apache 2.0) allow for "proprietarization" where a commercial entity can take the code, modify it, and keep those improvements secret. Conversely, strong copyleft licenses (like the GPL) can be overly restrictive, deterring commercial partners who might want to build complementary but proprietary tools.

The **MPL-2.0** is the superior choice because it offers a "file-level" copyleft. It ensures that any modifications to the library's core files must remain open source, protecting the public's investment in the software. However, it allows the library to be combined with proprietary software without forcing the proprietary code to be licensed under the MPL. This "best of both worlds" approach encourages government transparency while fostering a healthy ecosystem where private vendors can build value-added services.

## Patent Grants and Trademark Protections
Unlike the MIT license, which is silent on patents, the MPL-2.0 includes an explicit patent grant from all contributors. This is crucial for the Ministry of Education and other government bodies, as it provides a legal "safe harbor" against patent litigation from entities that have contributed to the library.

Furthermore, the MPL-2.0 maintains a clear distinction between copyright and trademark. This ensures that while the code is free to share, the "BOSC Community Library" brand and identity remain protected. This prevents bad actors from creating "look-alike" versions that could misinform the public or damage the library's reputation.

## Commercial Implications
A commercial entity wishing to build a "paid version" of the library can do so under the MPL-2.0, provided they respect the file-level copyleft. Specifically:
1. If they modify the core `src/` files, they MUST make those modifications available to the public.
2. They CAN build a separate proprietary application that *imports* and uses the BOSC library without having to open-source their entire product.
This model encourages the "Red Hat" style of business, where value is provided through support, integration, and proprietary extensions, rather than locking the core community-driven code behind a paywall.

---
*Date: May 11, 2026*
