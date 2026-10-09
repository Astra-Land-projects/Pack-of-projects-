🌍 Pack of Projects — A Universe of Ideas, Innovation & Technology

Welcome to Pack of Projects! 🚀

Pack of Projects is a multidisciplinary collection of projects, experiments, concepts, and practical solutions spanning a wide range of fields, technologies, and real-world applications.

Organized into 5 main folders containing approximately 100 projects each, this repository brings together an extensive collection of ideas covering technology, engineering, science, automation, digital solutions, and much more.

From artificial intelligence and robotics to electronics, mechanics, industrial systems, computer technology, migration-related tools, and innovative applications, Pack of Projects is a space for exploring ideas, solving problems, experimenting with new concepts, and building the future.

📂 Repository Structure

The repository is organized into five main folders, each containing approximately 100 projects.

Folder| Description
"folder1/"| Project collection 1
"folder2/"| Project collection 2
"folder3/"| Project collection 3
"folder4/"| Project collection 4
"folder5/"| Project collection 5

Replace these example folder names with the actual directory names in the repository.

🚀 Explore the World of Projects

Pack of Projects covers a broad range of fields and disciplines.

🤖 Artificial Intelligence & Intelligent Systems

AI applications, intelligent tools, automation concepts, machine learning experiments, and projects exploring emerging AI technologies.

⚡ Electronics & Electrical Engineering

Electronic circuits, components, control systems, electrical concepts, hardware experiments, and practical electronics applications.

🤖 Robotics & Automation

Robotic concepts, automated systems, control mechanisms, smart devices, and projects combining software with physical systems.

⚙️ Mechanical Engineering & Industrial Technology

Mechanical concepts, engineering experiments, industrial applications, manufacturing ideas, machinery-related projects, and process optimization.

💻 Computer Science & Software Development

Programming projects, algorithms, computational tools, software applications, computer systems, and digital solutions.

🌐 Web Development & Digital Platforms

Websites, interactive applications, digital tools, online platforms, and creative web-based experiences.

🧪 Science, Research & Experimentation

Scientific concepts, simulations, technical experiments, mathematical applications, and projects designed to explore how things work.

🏭 Industry, Manufacturing & Productivity

Industrial solutions, workflow improvements, operational tools, process automation, and ideas for improving efficiency.

🌍 Migration, International Opportunities & Digital Assistance

Projects exploring migration-related information, international opportunities, document organization, planning tools, and digital assistance for navigating complex processes.

Migration-related projects are informational or technical tools, not a substitute for official immigration guidance or professional legal advice.

💡 Innovation, Creativity & Emerging Technologies

Experimental concepts, futuristic ideas, unconventional applications, new approaches to existing problems, and projects exploring the possibilities of tomorrow.

🔧 Practical Tools & Everyday Applications

Useful utilities, calculators, organizational tools, productivity applications, and other projects designed to address practical needs.

🌱 And Much More

The collection is open to ideas across additional areas, including education, mathematics, physics, environmental technology, smart systems, data analysis, communication, energy, design, and interdisciplinary engineering.

These categories describe the intended scope of the collection; individual project contents and capabilities depend on what is actually implemented in each folder.

🎯 Our Mission

Pack of Projects aims to:

- Bring together projects from diverse technical and practical fields.
- Turn creative ideas into useful implementations and experiments.
- Explore the connections between software, hardware, science, and engineering.
- Encourage innovation, critical thinking, and multidisciplinary problem-solving.
- Develop practical tools and explore solutions to real-world challenges.
- Create an organized collection of projects that can grow and evolve over time.
- Support continuous learning through hands-on experimentation and development.

🧰 Technologies & Tools

Depending on the individual project, this repository may involve:

- Programming Languages: Python, JavaScript, PHP, C, C++, and others.
- Web Technologies: HTML, CSS, JavaScript, and backend frameworks.
- AI & Data Technologies: AI services, machine learning libraries, and data-processing tools.
- Electronics & Hardware: Microcontrollers, sensors, electronic components, and embedded systems.
- Engineering Tools: Simulation software, design tools, and technical applications.
- Automation & Robotics: Control software, automation techniques, and robotics-related technologies.

Not every project uses these technologies. Check each project's source code, documentation, and requirements before running it.

⚡ Getting Started

1. Clone or download the repository.
2. Explore the five project folders.
3. Choose a project that interests you.
4. Read its source code and available documentation.
5. Install the necessary tools, dependencies, or hardware components.
6. Follow the instructions specific to that project.
7. Experiment, learn, improve, and build upon the ideas where appropriate.

Some projects may run entirely in software, while others may require specialized hardware, external services, additional resources, or project-specific configuration.

🛡️ Responsible Innovation

Innovation should go hand in hand with responsibility.

Projects involving electronics, machinery, robotics, industrial systems, AI, or migration-related information should be evaluated carefully and used according to their intended purpose. Always follow relevant safety practices, protect sensitive information, and verify important decisions using reliable sources.

🌌 One Collection. Countless Possibilities.

Pack of Projects is more than an archive of code and ideas. It is a growing exploration of the many ways technology, science, engineering, and creativity can work together.

Every project can be a starting point: a question to investigate, a problem to solve, a concept to test, or an idea worth developing.

Explore widely. Think critically. Build creatively. Innovate without limits.

---

⭐ If you find the collection useful or inspiring, consider starring the repository on GitHub.

Part of the Astra-Land-projects organization.
----------------------------------
# Astra Global Migration — Global Migration Portfolio

90 پروژه مستقل و قابل اجرا برای USA، Türkiye، UK، Europe (و هاب‌های Germany، France، Italy، Spain، Netherlands).

## اجرا
- **لابی:** `index.html` را باز کنید (یا `python3 -m http.server 8000` در همین پوشه).
- **هر پروژه به‌تنهایی:** وارد پوشه پروژه شوید و `index.html` را باز کنید؛ هر پوشه فایل‌های کامل خودش (`index.html`، `app.js`، `style.css`، `data.js`، `README.md`) را دارد و می‌تواند جداگانه کپی یا دیپلوی شود.
- **API اختیاری (FastAPI + SQLite، آماده Docker):**
  ```bash
  cd backend && pip install -r requirements.txt && uvicorn app:app --port 8000
  # یا: cd backend && docker compose up --build   → http://localhost:8080
  ```
  Endpoints: `/api/projects`, `/api/projects/{slug}`, `/api/sources`, `POST /api/monitor/run`, `/api/monitor/changes`

## معماری
- Frontend: Vanilla JS بدون وابستگی، RTL، حالت تاریک، چاپ‌پذیر
- ذخیره‌سازی: localStorage + IndexedDB؛ گاوصندوق‌ها با AES-GCM 256 (Web Crypto)
- AI: بازیابی محلی (RAG-lite) روی پایگاه دانش منابع رسمی + اتصال اختیاری به LLM سازگار با OpenAI
- پایش منابع: `monitor.py` (کتابخانه استاندارد پایتون) و API سمت سرور
- هر ادعا به منبع رسمی لینک شده و تاریخ بازبینی (2026-10-01) نمایش داده می‌شود

## فهرست پروژه‌ها
| منطقه | پروژه | توضیح | نوع |
|---|---|---|---|
| USA | [USA Migration Hub](usa-migration-hub/) | مرکز ابزارهای مهاجرتی آمریکا | هاب کشوری |
| USA | [USA Visa Navigator](usa-visa-navigator/) | انتخاب مسیر ویزا بر اساس هدف، تحصیل، کار و خانواده | مسیریاب (rule-based matching) |
| USA | [US Immigration Route Explorer](us-immigration-route-explorer/) | مسیر احتمالی از ورود تا اقامت دائم | تایم‌لاین مسیر |
| USA | [USCIS Case Tracker Pro](uscis-case-tracker-pro/) | پیگیری حرفه‌ای پرونده‌ها با تاریخچه، تایم‌لاین و یادآوری | ردیاب پرونده |
| USA | [USCIS Case Timeline Visualizer](uscis-case-timeline-visualizer/) | تبدیل وضعیت پرونده به تایم‌لاین گرافیکی | مصورساز تایم‌لاین |
| USA | [US Immigration Document Builder](us-immigration-document-builder/) | ساخت چک‌لیست مدارک بر اساس نوع پرونده | چک‌لیست مدارک |
| USA | [US Visa Wait Time Dashboard](us-visa-wait-time-dashboard/) | داشبورد زمان انتظار ویزا بر اساس کنسولگری و نوع ویزا | داشبورد زمان انتظار |
| USA | [US Immigration Cost Calculator](us-immigration-cost-calculator/) | برآورد هزینه‌های اداری، ترجمه، سفر و سایر هزینه‌ها | ماشین‌حساب هزینه |
| USA | [US Student Migration Planner](us-student-migration-planner/) | برنامه‌ریزی تحصیل ← کار ← ماندن در آمریکا (بدون ادعای تضمین) | برنامه‌ریز زمان‌بندی‌شده |
| USA | [US Sponsor Job Finder](us-sponsor-job-finder/) | جست‌وجوی موقعیت‌های شغلی مرتبط با sponsorship | جست‌وجو + ردیاب |
| USA | [US CV → Job Match AI](us-cv-job-match-ai/) | تحلیل رزومه و مقایسه با آگهی شغلی برای بازار آمریکا | تحلیل/تطبیق رزومه |
| USA | [US Immigration News Monitor](us-immigration-news-monitor/) | پایش و دسته‌بندی تغییرات رسمی | پایش منابع رسمی |
| USA | [US Case Document Vault](us-case-document-vault/) | مدیریت امن اسناد، تاریخ انقضا و چک‌لیست | گاوصندوق رمزگذاری‌شده |
| USA | [Astra USA Immigration Copilot](astra-usa-immigration-copilot/) | پروفایل ← مسیرها ← مدارک ← ددلاین ← هزینه ← شغل/دانشگاه ← منابع رسمی | کوپایلت + RAG |
| Türkiye | [Türkiye Migration Hub](turkiye-migration-hub/) | مرکز ابزارهای مهاجرتی ترکیه | هاب کشوری |
| Türkiye | [Türkiye Residence Explorer](turkiye-residence-explorer/) | معرفی و مقایسه انواع اقامت ترکیه | اکسپلورر + محاسبه‌گر |
| Türkiye | [e-İkamet Assistant](e-ikamet-assistant/) | راهنمای مرحله‌به‌مرحله فرآیند آنلاین اقامت | راهنمای مرحله‌ای |
| Türkiye | [Türkiye Residence Document Checklist](turkiye-residence-document-checklist/) | چک‌لیست مدارک اقامت ترکیه | چک‌لیست مدارک |
| Türkiye | [Residence Renewal Reminder](turkiye-residence-renewal-reminder/) | یادآوری زمان تمدید اقامت | مدیر ددلاین |
| Türkiye | [Türkiye Visa Checker](turkiye-visa-checker/) | بررسی اولیه نیاز به ویزا بر اساس تابعیت و نوع سفر | مسیریاب (rule-based matching) |
| Türkiye | [Türkiye e-Visa Assistant](turkiye-e-visa-assistant/) | راهنمای استفاده از پورتال رسمی e-Visa | راهنمای مرحله‌ای |
| Türkiye | [Türkiye Relocation Planner](turkiye-relocation-planner/) | برنامه انتقال به ترکیه | برنامه‌ریز زمان‌بندی‌شده |
| Türkiye | [Türkiye Cost of Living Calculator](turkiye-cost-of-living-calculator/) | مقایسه شهرها و هزینه‌های زندگی ترکیه | هزینه زندگی |
| Türkiye | [Türkiye Student Migration Planner](turkiye-student-migration-planner/) | تحصیل و برنامه‌ریزی زندگی دانشجویی در ترکیه | برنامه‌ریز زمان‌بندی‌شده |
| Türkiye | [Türkiye Job & Residence Matcher](turkiye-job-residence-matcher/) | اتصال مسیر شغلی به نوع اقامت/مجوز | مسیریاب (rule-based matching) |
| Türkiye | [Türkiye Immigration Document Vault](turkiye-immigration-document-vault/) | مدیریت امن اسناد مهاجرتی ترکیه | گاوصندوق رمزگذاری‌شده |
| Türkiye | [Türkiye Immigration Scam Detector](turkiye-immigration-scam-detector/) | تشخیص سایت‌ها، دامنه‌ها و ادعاهای مشکوک | تشخیص کلاهبرداری |
| UK | [UK Migration Hub](uk-migration-hub/) | مرکز ابزارهای بریتانیا | هاب کشوری |
| UK | [UK Visa Navigator](uk-visa-navigator/) | پیدا کردن مسیر ویزای بریتانیا | مسیریاب (rule-based matching) |
| UK | [UK Student Route Planner](uk-student-route-planner/) | برنامه تحصیل در بریتانیا | برنامه‌ریز زمان‌بندی‌شده |
| UK | [UK Skilled Work Explorer](uk-skilled-work-explorer/) | بررسی اطلاعات مسیر Skilled Worker | اکسپلورر + محاسبه‌گر |
| UK | [UK Visa Document Checklist](uk-visa-document-checklist/) | چک‌لیست مدارک ویزای بریتانیا | چک‌لیست مدارک |
| UK | [UK eVisa Dashboard](uk-evisa-dashboard/) | مدیریت وضعیت eVisa و share code | ردیاب پرونده |
| UK | [UK Visa Timeline Tracker](uk-visa-timeline-tracker/) | تایم‌لاین پرونده ویزای UK | تایم‌لاین مسیر |
| UK | [UK Cost of Relocation](uk-cost-of-relocation/) | برآورد هزینه انتقال به بریتانیا | ماشین‌حساب هزینه |
| UK | [UK Job Sponsorship Finder](uk-job-sponsorship-finder/) | جست‌وجوی مشاغل مرتبط با sponsorship | جست‌وجو + ردیاب |
| UK | [UK CV Analyzer AI](uk-cv-analyzer-ai/) | تحلیل رزومه برای بازار بریتانیا | تحلیل/تطبیق رزومه |
| UK | [UK University Migration Planner](uk-university-migration-planner/) | تحصیل + برنامه‌ریزی شغلی در UK | برنامه‌ریز زمان‌بندی‌شده |
| UK | [UK Immigration Source Monitor](uk-immigration-source-monitor/) | پایش تغییرات منابع رسمی بریتانیا | پایش منابع رسمی |
| UK | [UK Settlement Journey Planner](uk-settlement-journey-planner/) | مراحل و ددلاین‌های مسیر اقامت دائم (ILR) و شهروندی | تایم‌لاین مسیر |
| Europe | [Europe Migration Hub](europe-migration-hub/) | مرکز ابزارهای اروپا | هاب کشوری |
| Europe | [EU Migration Navigator](eu-migration-navigator/) | مسیرها، مدارک، هزینه و منابع رسمی کشورهای اروپایی | کوپایلت + RAG |
| Europe | [EU Blue Card Explorer](eu-blue-card-explorer/) | مقایسه اطلاعات Blue Card کشورهای مختلف | اکسپلورر + محاسبه‌گر |
| Europe | [EU Immigration Country Compare](eu-immigration-country-compare/) | مقایسه چند کشور اروپایی در یک داشبورد | مقایسه کشورها |
| Europe | [Europe Work Mobility AI](europe-work-mobility-ai/) | پیدا کردن کشورها/بازارهای مرتبط با مهارت شما | تطبیق بازار کار |
| Europe | [EURES Job Matcher AI](eures-job-matcher-ai/) | تطبیق رزومه با مشاغل اروپایی | تحلیل/تطبیق رزومه |
| Europe | [Europe CV Converter](europe-cv-converter/) | تبدیل رزومه به قالب‌های کشورهای مختلف | مبدل رزومه |
| Europe | [EU Qualification Navigator](eu-qualification-navigator/) | راهنمای شناسایی و معادل‌سازی مدارک | مسیریاب (rule-based matching) |
| Europe | [Europe Document Checklist](europe-document-checklist/) | مدارک موردنیاز بر اساس کشور و هدف | چک‌لیست مدارک |
| Europe | [EU Relocation Planner](eu-relocation-planner/) | برنامه کامل relocation به اروپا | برنامه‌ریز زمان‌بندی‌شده |
| Europe | [Europe Cost of Living Map](europe-cost-of-living-map/) | مقایسه هزینه زندگی شهرهای اروپا | هزینه زندگی |
| Europe | [Europe Student Route Finder](europe-student-route-finder/) | جست‌وجوی مسیرهای تحصیلی اروپا | مسیریاب (rule-based matching) |
| Europe | [Europe Scholarship Finder](europe-scholarship-finder/) | موتور جست‌وجوی بورسیه | جست‌وجوی بورسیه |
| Europe | [Europe Job Mobility Dashboard](europe-job-mobility-dashboard/) | داشبورد فرصت‌های کاری و جابه‌جایی | جست‌وجو + ردیاب |
| Europe | [EU Cross-Border Worker Assistant](eu-cross-border-worker-assistant/) | اطلاعات کار بین کشورهای مرزی | مسیریاب (rule-based matching) |
| Europe | [Europe Migration Deadline Manager](europe-migration-deadline-manager/) | مدیریت ددلاین‌های مهاجرت اروپا | مدیر ددلاین |
| Europe | [Europe Immigration Source Tracker](europe-immigration-source-tracker/) | ذخیره و پایش منابع رسمی هر کشور | پایش منابع رسمی |
| Germany | [Germany Migration Hub](germany-migration-hub/) | مرکز ابزارهای آلمان | هاب کشوری |
| Germany | [Opportunity Card Explorer](germany-opportunity-card-explorer/) | محاسبه امتیاز Chancenkarte (کارت فرصت) | محاسبه امتیاز |
| Germany | [Germany Student Planner](germany-student-planner/) | برنامه تحصیل در آلمان | برنامه‌ریز زمان‌بندی‌شده |
| Germany | [Germany Job Matcher AI](germany-job-matcher-ai/) | تطبیق رزومه با آگهی‌های آلمان | تحلیل/تطبیق رزومه |
| Germany | [Germany Document Checklist](germany-document-checklist/) | چک‌لیست مدارک ویزای آلمان | چک‌لیست مدارک |
| Germany | [Germany Cost Calculator](germany-cost-calculator/) | برآورد هزینه مهاجرت به آلمان | ماشین‌حساب هزینه |
| Germany | [Germany Residence Timeline](germany-residence-timeline/) | تایم‌لاین اقامت آلمان تا اقامت دائم/شهروندی | تایم‌لاین مسیر |
| Germany | [Germany CV Analyzer](germany-cv-analyzer/) | تحلیل رزومه برای بازار آلمان | تحلیل/تطبیق رزومه |
| France | [France Migration Hub](france-migration-hub/) | مرکز ابزارهای فرانسه | هاب کشوری |
| France | [France Student Route](france-student-route/) | مسیر تحصیل در فرانسه (Études en France) | برنامه‌ریز زمان‌بندی‌شده |
| France | [France Work Route Explorer](france-work-route-explorer/) | بررسی مسیرهای کاری فرانسه | مسیریاب (rule-based matching) |
| France | [France Document Manager](france-document-manager/) | مدیریت امن اسناد مهاجرتی فرانسه | گاوصندوق رمزگذاری‌شده |
| France | [France CV Matcher](france-cv-matcher/) | تطبیق رزومه با آگهی‌های فرانسه | تحلیل/تطبیق رزومه |
| France | [France Relocation Planner](france-relocation-planner/) | برنامه انتقال به فرانسه | برنامه‌ریز زمان‌بندی‌شده |
| France | [France Cost of Living Tool](france-cost-of-living-tool/) | مقایسه هزینه زندگی شهرهای فرانسه | هزینه زندگی |
| Italy | [Italy Migration Hub](italy-migration-hub/) | مرکز ابزارهای ایتالیا | هاب کشوری |
| Italy | [Italy Student Migration](italy-student-migration/) | برنامه تحصیل در ایتالیا | برنامه‌ریز زمان‌بندی‌شده |
| Italy | [Italy Work Opportunity Finder](italy-work-opportunity-finder/) | جست‌وجوی فرصت‌های کاری ایتالیا | جست‌وجو + ردیاب |
| Italy | [Italy Scholarship Finder](italy-scholarship-finder/) | موتور جست‌وجوی بورسیه ایتالیا | جست‌وجوی بورسیه |
| Italy | [Italy Document Checklist](italy-document-checklist/) | چک‌لیست مدارک ایتالیا | چک‌لیست مدارک |
| Italy | [Italy Relocation Calculator](italy-relocation-calculator/) | برآورد هزینه انتقال به ایتالیا | ماشین‌حساب هزینه |
| Spain | [Spain Migration Hub](spain-migration-hub/) | مرکز ابزارهای اسپانیا | هاب کشوری |
| Spain | [Spain Student Planner](spain-student-planner/) | برنامه تحصیل در اسپانیا | برنامه‌ریز زمان‌بندی‌شده |
| Spain | [Spain Work Route Explorer](spain-work-route-explorer/) | بررسی مسیرهای کاری اسپانیا | مسیریاب (rule-based matching) |
| Spain | [Spain Digital Nomad Information Hub](spain-digital-nomad-information-hub/) | اطلاعات ویزای دیجیتال نومد اسپانیا | اکسپلورر + محاسبه‌گر |
| Spain | [Spain Cost Calculator](spain-cost-calculator/) | برآورد هزینه مهاجرت به اسپانیا | ماشین‌حساب هزینه |
| Spain | [Spain Document Manager](spain-document-manager/) | مدیریت امن اسناد اسپانیا | گاوصندوق رمزگذاری‌شده |
| Netherlands | [Netherlands Migration Hub](netherlands-migration-hub/) | مرکز ابزارهای هلند | هاب کشوری |
| Netherlands | [Netherlands Study Planner](netherlands-study-planner/) | برنامه تحصیل در هلند | برنامه‌ریز زمان‌بندی‌شده |
| Netherlands | [Netherlands Job Matcher](netherlands-job-matcher/) | تطبیق رزومه با آگهی‌های هلند + بررسی sponsor | تحلیل/تطبیق رزومه |
| Netherlands | [Netherlands Residence Planner](netherlands-residence-planner/) | تایم‌لاین اقامت هلند | تایم‌لاین مسیر |
| Netherlands | [Netherlands Housing Search Dashboard](netherlands-housing-search-dashboard/) | داشبورد جست‌وجوی مسکن هلند | جست‌وجو + ردیاب |
| Netherlands | [Netherlands Relocation Cost Calculator](netherlands-relocation-cost-calculator/) | برآورد هزینه انتقال به هلند | ماشین‌حساب هزینه |

## سلب مسئولیت
ابزارها «مطابقت اولیه با معیارهای منتشرشده» ارائه می‌دهند و مشاوره حقوقی یا تضمین نتیجه نیستند.
