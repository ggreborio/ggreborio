
# Hi, my name is Georgette 👋

Master's student in Health Data Science (BA in Psychology, minors in Computer
Science and Health Studies). I use data to study health behavior and outcomes,
and I'm interested in hospital outcomes, data privacy and social health disparities.

**Skills:** R · Python · SQL · C · Java · Git · R Markdown / Quarto · Orange Data Mining 

**Contact:** [LinkedIn](https://www.linkedin.com/in/georgettegreborio/) · georgette.greborio@outlook.com

### IN PROGRESS: Behavior Data Analysis in a Public School Setting [view in progress](behavior-data-portfolio) · [notebook](behavior-data-portfolio/analysis.ipynb)
##### Working as a Registered Behavior Technician in public schools, I tracked daily behavior data for a student in a general education classroom, and the visualized data was used to support a request for a more specialized placement. To recreate that work for my portfolio without any real student information, I had Claude write Python script that generates a fully synthetic dataset for a fictional student and then I wrote code to analyze it in Jupyter with pandas, matplotlib, and seaborn. The data covers 50 school days of off-task behavior, demand refusal, elopement, and unsafe physical behavior, along with reinforcer points, a low demand day indicator, and progress on three IEP-style goals measured against an 80% mastery threshold. I reshaped the data between wide and long formats, compared behavior on low demand and regular days with box plots, summarized weekly and weekday patterns as percent differences from the student's own average, and tracked goal progress against the threshold [add your result, for example "none of the three goals reached 80% on three consecutive days"]. Behavior counts were lower on low demand days, most clearly for off-task behavior. Because the data is synthetic, these patterns reflect how it was generated, and each weekday average rests on only ten days, so the findings are descriptive rather than causal.

### ED Triage and ICU Admission Analysis [project folder](NHAMCS%20Project) · [full analysis (HTML)](NHAMCS%20Project/nhamcs_analysis.html)
##### For an epidemiology data management course, I first built a REDCap data collection system for studying emergency department triage and ICU admission, then extended the project to the full 2022 National Hospital Ambulatory Medical Care Survey (NHAMCS), a CDC dataset of over 16,000 ED visits. Working in R and Quarto, I read the Stata file directly with haven, recoded the survey's special missing-value codes, and built a binary ICU outcome from the admission-unit variable, checking it against a second admission variable. I used logistic regression to examine how triage urgency and age relate to ICU admission, and combined sparsely populated triage groups so the estimates were stable. The analysis showed that ICU admission rose with triage urgency and that older age was associated with higher odds of ICU admission after adjusting for triage. The results are unweighted and describe the sample rather than national estimates, so I documented that and other limitations in the report.

### Economic and Environmental Visualization Project [view final report](econ-environment-project/BSDS%20Final%20Team%20Report.pdf)
##### For a group project in my Data Science course, I collaborated with my team to analyze the relationship between economic inequality and environmental health using global datasets from the World Bank. We cleaned, merged, and analyzed economic and environmental indicators for over 180 countries using R and R Markdown. I led the climate change analysis, examining how greenhouse gas emissions varied across income groups through data wrangling, exploratory analysis, and visualizations including bar plots and boxplots. My analysis revealed that lower-income countries often experience higher and more variable emissions, highlighting how environmental harm disproportionately affects economically disadvantaged regions.


### Hashmap Project [view code](systems-programming/hashmap)
##### For a semester-long final project in my C and Systems Programming course, I implemented a custom hash map from scratch in C and designed the core data structures, including linked lists for collision handling, and implemented key operations such as insertion, lookup, deletion, and dynamic resizing based on load factor thresholds. The map used SHA-256 hashing to generate indices and needed careful memory management, including reallocation and deallocation. I developed and tested the project entirely in the terminal using GCC, debugging segmentation faults and logic errors. This project strengthened my understanding of low-level systems concepts, data structures, and the tradeoffs involved in performance, scalability, and memory safety.


### File System Java Project [view code](systems-programming/file-system)
##### Developed a Java-based command-line file system simulator that models a hierarchical directory structure using tree-based data structures. The system supports custom command-line operations for creating, navigating, searching, and managing files and directories entirely in memory. The project emphasizes object-oriented design, recursion, and parent–child directory relationships to enable directory traversal, path construction, and aggregate file size calculations.


### Biological Psychology Final Paper [read the paper](biological-psychology-paper/Biology%20Final%20Paper.pdf)
#### For a Biological Psychology research paper, I explored how disruptions to circadian rhythms can affect weight regulation and metabolic health. I reviewed and synthesized research on sleep–wake cycles, hormonal regulation, and autonomic nervous system activity to understand links to obesity and type 2 diabetes. Through this project, I connected biological mechanisms like melatonin secretion and glucose regulation to real-world health outcomes, strengthening my ability to evaluate scientific literature and clearly explain complex concepts.


