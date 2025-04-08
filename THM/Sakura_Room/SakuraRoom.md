# :cherry_blossom: TryHackMe: Sakura — OSINT Room Writeup

**Author:** B0bTheSkull  
**Room URL:** [TryHackMe - Sakura](https://tryhackme.com/room/sakura)  
**Date Completed:** YYYY-MM-DD  
**Category:** OSINT  
**Difficulty:** Easy/Medium/Hard  
**Tags:** OSINT, Social Media, Image Analysis, Google-Fu

---

## 1. Approach & Mindset :bulb:

> Brief summary of the room’s theme.    
> *“This room drops you into a hands-on digital manhunt, testing a wide range of OSINT techniques. Built for beginners but grounded in real-world tactics, you’ll follow a staged investigation to track down a cybercriminal—one clue at a time. Each challenge gives you just enough pretext to start digging, and it’s your job to connect the dots using social media sleuthing, image forensics, and pure recon grit. Think of it as a virtual stakeout with zero paperwork.”*

---

## 2. Tools Used :hammer:

- [ ] Google (dorking, image search)
- [ ] EXIF Viewer (e.g., `exiftool`, https://www.metadata2go.com/)
- [ ] Social Media Scrapers (e.g., WhatsMyName, Sherlock)
- [ ] Reverse Image Search (Google, Yandex, TinEye)
- [ ] GeoGuessr Skills™️ (a.k.a. map detective work)
- [ ] WHOIS / DNS tools
- [ ] Common sense & digital intuition

---
### TIP-OFF
**Question:** _What username does the attacker go by?_  
**Answer:** `Username`

**How I found it:**
- The room provides you with the following clue: 
![Alt](./photos/sakurapwnedletter.png)
- Started on [platform/page]
- Found username: `@xSakuraGirl1997`
- Used Sherlock to check across platforms
- Profile pic reverse searched → led to LinkedIn profile

---

### ✅ Task 2: [e.g., Where is she located?]
**Answer:** `Tokyo, Japan`

**Method:**
- Pulled EXIF metadata from uploaded image → GPS hidden
- Analyzed background landmarks → matched to [place]
- Confirmed via Google Maps + street view

---

### ✅ Task 3: [e.g., What is her email?]
**Answer:** `sakura.fox93@gmail.com`

**Steps Taken:**
- Checked about sections, GitHub bio, and blog contact pages
- Used `hunter.io` and `EmailRep.io` for extra validation
- Cross-referenced with known breaches (optional)

---

### ✅ Task 4: [e.g., What platform was her blog hosted on?]
**Answer:** `WordPress`

**How I found it:**
- Blog URL ending in `/wp-content/`
- Used `WhatCMS.org` to verify

---

### ✅ Final Flag:
```plaintext
THM{final_flag_value}