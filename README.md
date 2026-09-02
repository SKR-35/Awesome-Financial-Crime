![Awesome](https://img.shields.io/badge/Awesome-List-6F42C1?logo=awesomelists&logoColor=white)
[![CI - Link Check](https://img.shields.io/github/actions/workflow/status/SKR-35/Awesome-Financial-Crime/link-check.yml?branch=master&label=CI%20-%20Link%20Check&logo=githubactions&logoColor=white)](https://github.com/SKR-35/Awesome-Financial-Crime/actions/workflows/link-check.yml)

# Awesome Financial Crime

A curated list of Financial Crime Compliance (FCC) resources: transaction monitoring, trade surveillance, e-comms surveillance, fraud detection, case management, sanctions screening, KYC/KYB, graph analytics, datasets, regulations and more.

Financial crime spans AML/CFT, sanctions, AB&C, market abuse, fraud and investigative tooling. This list aims to be practical, vendor-neutral and signal-rich.

## Table of Contents

- [Vendor / Commercial Platforms](#vendor--commercial-platforms)
- [Transaction Monitoring (AML)](#transaction-monitoring-aml)
- [Trade Surveillance (Market Abuse)](#trade-surveillance-market-abuse)
- [E-Comms / Conduct Surveillance](#e-comms--conduct-surveillance)
- [Fraud Detection](#fraud-detection)
- [Sanctions & Screening](#sanctions--screening)
- [KYC / KYB / Customer Risk](#kyc--kyb--customer-risk)
- [Case Management & Investigation](#case-management--investigation)
- [Graph & Link Analysis](#graph--link-analysis)
- [Graph Machine Learning](#graph-machine-learning)
- [Entity Resolution & Master Data](#entity-resolution--master-data)
- [Data Ingestion, ETL & Quality](#data-ingestion-etl--quality)
- [Synthetic Data & Simulators](#synthetic-data--simulators)
- [MLOps, Monitoring & Drift Detection](#mlops-monitoring--drift-detection)
- [Feature Engineering & Feature Store](#feature-engineering--feature-store)
- [Explainability & Model Risk](#explainability--model-risk)
- [Benchmarks & Datasets](#benchmarks--datasets)
- [Certifications](#certifications)
- [Books](#books)
- [Documentaries, Movies & TV Series](#documentaries-movies--tv-series)
- [Typologies](#typologies)
- [Regulations, Standards & Guidance](#regulations-standards--guidance)

## Vendor / Commercial Platforms

Commercial tools are useful for discovery:

- Oracle Financial Crime and Compliance Management (FCCM) Solutions - Enterprise AML transaction monitoring/Mantas & case mgmt.

	- <a href="https://www.oracle.com/financial-services/aml-financial-crime-compliance/" target="_blank" rel="noopener noreferrer">Official Page</a>

- NICE Actimize - Cross-domain FCC suite (AML, fraud, trade/e-comms).

	- <a href="https://www.niceactimize.com/" target="_blank" rel="noopener noreferrer">Official Page</a>

- SAS AML / Fraud - Analytics-driven FCC platform.

	- <a href="https://www.sas.com/en_us/home.html" target="_blank" rel="noopener noreferrer">Official Page</a>
	
	- <a href="https://github.com/sassoftware" target="_blank" rel="noopener noreferrer">GitHub</a>

- SymphonyAI NetReveal - AML, fraud and KYC risk.

	- <a href="https://www.symphonyai.com/financial-services/netreveal-transaction-monitoring/" target="_blank" rel="noopener noreferrer">Official Page</a>
	
	- <a href="https://github.com/symphonyai-accelerate" target="_blank" rel="noopener noreferrer">GitHub</a>

- Quantexa - Entity resolution & network analytics.

	- <a href="https://www.quantexa.com/" target="_blank" rel="noopener noreferrer">Official Page</a>

- Featurespace - Adaptive behavioral fraud analytics.

	- <a href="https://www.featurespace.com/" target="_blank" rel="noopener noreferrer">Official Page</a>
	
	- <a href="https://github.com/Featurespace" target="_blank" rel="noopener noreferrer">GitHub</a>

- Behavox / Shield / Smarsh - E-comms surveillance stacks.

	- <a href="https://www.behavox.com/" target="_blank" rel="noopener noreferrer">Behavox Official Page</a>
	
	- <a href="https://www.shieldfc.com/" target="_blank" rel="noopener noreferrer">Shield Official Page</a>
	
	- <a href="https://www.smarsh.com/" target="_blank" rel="noopener noreferrer">Smarsh Official Page</a>
	
	- <a href="https://github.com/smarsh" target="_blank" rel="noopener noreferrer">Smarsh GitHub</a>

- Solidus / ACA / QuestDB - Trade surveillance.

	- <a href="https://www.soliduslabs.com/solutions/trade-surveillance" target="_blank" rel="noopener noreferrer">Solidus Official Page</a>
	
	- <a href="https://www.acaglobal.com/technology/surveillance-monitoring/market-abuse-surveillance/" target="_blank" rel="noopener noreferrer">ACA Official Page</a>
	
	- <a href="https://questdb.com/glossary/real-time-trade-surveillance/" target="_blank" rel="noopener noreferrer">QuestDB Official Page</a>
	
	- <a href="https://github.com/questdb" target="_blank" rel="noopener noreferrer">QuestDB GitHub</a>
	
- Elliptic - Wallet & transaction screening for AML compliance
 	- <a href="https://www.elliptic.co/solutions/screening" target="_blank" rel="noopener noreferrer">Official Page</a>
	
- [AI DECISIONS](https://aidecisions.ai) - Multi-chain wallet screening API (Ethereum, Bitcoin, Tron, Base, Arbitrum, Gnosis): sanctions, mixer exposure, risk tier; free tier and a free public checker.

## Transaction Monitoring (AML)

- Apache Flink - Streaming engine for real-time TM pipelines. 
	- <a href="https://github.com/apache/flink" target="_blank" rel="noopener noreferrer">GitHub</a>
	
- Drools - Business rules engine suitable for deterministic AML transaction-monitoring scenarios and rule-based alerting.

    - <a href="https://github.com/kiegroup/drools" target="_blank" rel="noopener noreferrer">GitHub</a>

- Apache Kafka - Event streaming platform for high-volume transaction ingestion and near-real-time monitoring pipelines.

    - <a href="https://github.com/apache/kafka" target="_blank" rel="noopener noreferrer">GitHub</a>

- Apache Spark - Distributed processing framework for large-scale transaction monitoring, feature engineering and batch detection.

    - <a href="https://github.com/apache/spark" target="_blank" rel="noopener noreferrer">GitHub</a>

## Trade Surveillance (Market Abuse)

- TimescaleDB - Time-series SQL for order book analytics.

	- <a href="https://github.com/timescale/timescaledb" target="_blank" rel="noopener noreferrer">GitHub</a>
	
- QuestDB - High-performance time-series database suitable for market data, order-book and surveillance analytics.

    - <a href="https://github.com/questdb/questdb" target="_blank" rel="noopener noreferrer">GitHub</a>

- Apache Kafka - Streaming infrastructure for market-data and order-event ingestion.

    - <a href="https://github.com/apache/kafka" target="_blank" rel="noopener noreferrer">GitHub</a>

- Polars - High-performance dataframe library useful for large-scale order and trade surveillance analytics.

    - <a href="https://github.com/pola-rs/polars" target="_blank" rel="noopener noreferrer">GitHub</a>

## E-Comms / Conduct Surveillance

- spaCy / Hugging Face - NLP pipelines for policy violations, collusion cues.

	- <a href="https://github.com/explosion/spaCy" target="_blank" rel="noopener noreferrer">spaCy GitHub</a>
	
	- <a href="https://github.com/huggingface" target="_blank" rel="noopener noreferrer">Hugging Face GitHub</a>

## Fraud Detection

- PyOD - Outlier detection toolbox for fraud features.

	- <a href="https://github.com/yzhao062/pyod" target="_blank" rel="noopener noreferrer">GitHub</a>

- River - Online ML for streaming fraud detection.

	- <a href="https://riverml.xyz/" target="_blank" rel="noopener noreferrer">Official Page</a>

	- <a href="https://github.com/online-ml/river" target="_blank" rel="noopener noreferrer">River GitHub</a>

- XGBoost / LightGBM - Gradient boosting baselines for tabular fraud.

	- <a href="https://github.com/dmlc/xgboost" target="_blank" rel="noopener noreferrer">xgboost GitHub</a>
	
	- <a href="https://github.com/microsoft/LightGBM" target="_blank" rel="noopener noreferrer">LightGBM GitHub</a>

## Sanctions & Screening

- OpenSanctions - Sanctions & PEPs knowledge graph + entity data pipelines.

	- <a href="https://www.opensanctions.org/" target="_blank" rel="noopener noreferrer">Official Page</a>
	
	- <a href="https://github.com/opensanctions/opensanctions" target="_blank" rel="noopener noreferrer">GitHub</a>

- FuzzyWuzzy / RapidFuzz - Name-matching baseline.

	- <a href="https://github.com/seatgeek/fuzzywuzzy" target="_blank" rel="noopener noreferrer">FuzzyWuzzy GitHub</a>
	
	- <a href="https://github.com/rapidfuzz/RapidFuzz" target="_blank" rel="noopener noreferrer">RapidFuzzy GitHub</a>

- OFAC SDN & Consolidated Lists - Official lists + update cadence, formats.

	- <a href="https://sanctionslist.ofac.treas.gov/Home/ConsolidatedList" target="_blank" rel="noopener noreferrer">Official Page</a>

## KYC / KYB / Customer Risk

- Great Expectations - Data quality gates for KYC feeds.

	- <a href="https://github.com/great-expectations/great_expectations" target="_blank" rel="noopener noreferrer">GitHub</a>
	
- OpenSanctions - Open-source sanctions, PEP and entity data useful for customer screening and risk assessment.

    - <a href="https://github.com/opensanctions/opensanctions" target="_blank" rel="noopener noreferrer">GitHub</a>

- Splink - Probabilistic entity resolution for customer deduplication and identity matching.

    - <a href="https://github.com/moj-analytical-services/splink" target="_blank" rel="noopener noreferrer">GitHub</a>

- RapidFuzz - Fast fuzzy string matching useful for names, aliases and customer-record comparison.

    - <a href="https://github.com/rapidfuzz/RapidFuzz" target="_blank" rel="noopener noreferrer">GitHub</a>

## Case Management & Investigation

- Kibana/Elasticsearch - Query, pivot and visualize alert context.

	- <a href="https://github.com/elastic/kibana" target="_blank" rel="noopener noreferrer">Kibana GitHub</a>
	
	- <a href="https://github.com/elastic/elasticsearch" target="_blank" rel="noopener noreferrer">Elasticsearch GitHub</a>

- OpenSearch - Elastic alternative for investigations.
	
	- <a href="https://github.com/opensearch-project/OpenSearch" target="_blank" rel="noopener noreferrer">OpenSearch GitHub</a>
	
- Apache Superset - Investigation dashboards.
	
	- <a href="https://github.com/apache/superset" target="_blank" rel="noopener noreferrer">Apache Superset GitHub</a>

## Graph & Link Analysis

- NetworkX - Graph feature engineering (centrality, motifs).

	- <a href="https://github.com/networkx/networkx" target="_blank" rel="noopener noreferrer">GitHub</a>

- Neo4j - Labeled-property graph DB for rings & money-mules.

	- <a href="https://github.com/neo4j/neo4j" target="_blank" rel="noopener noreferrer">GitHub</a>

- Memgraph - Real-time graph with Cypher for streaming rings.

	- <a href="https://github.com/memgraph/memgraph" target="_blank" rel="noopener noreferrer">GitHub</a>

- Graphistry - GPU visual analytics on alert clusters.

	- <a href="https://github.com/graphistry" target="_blank" rel="noopener noreferrer">GitHub</a>
	
## Graph Machine Learning

- PyTorch Geometric - Graph neural networks for AML/fraud rings.

	- <a href="https://github.com/pyg-team/pytorch_geometric" target="_blank" rel="noopener noreferrer">GitHub</a>

- DGL (Deep Graph Library) - Scalable graph learning.

	- <a href="https://github.com/dmlc/dgl" target="_blank" rel="noopener noreferrer">GitHub</a>
  
- [openheads](https://github.com/ai-decisions/openheads) - Training code for a GNN financial-crime detector over a multi-chain transaction graph (warm-start recipe, threshold calibration), Apache-2.0.	

## Entity Resolution & Master Data

- Splink - Probabilistic entity resolution at scale.

	- <a href="https://github.com/moj-analytical-services/splink" target="_blank" rel="noopener noreferrer">GitHub</a>
	
- Dedupe - Python entity resolution library.

	- <a href="https://github.com/dedupeio/dedupe" target="_blank" rel="noopener noreferrer">GitHub</a>

## Data Ingestion, ETL & Quality

- Airflow - Batch orchestration for financial crime pipelines.

	- <a href="https://github.com/apache/airflow" target="_blank" rel="noopener noreferrer">GitHub</a>
	
- Soda - Data quality testing and monitoring.

	- <a href="https://github.com/sodadata/soda-core" target="_blank" rel="noopener noreferrer">GitHub</a> 

- Pandera - Data validation for pandas pipelines.

	- <a href="https://github.com/unionai-oss/pandera" target="_blank" rel="noopener noreferrer">GitHub</a> 

## Synthetic Data & Simulators

- SDV (Synthetic Data Vault) - Tabular synthetic data generation for model dev.

	- <a href="https://github.com/sdv-dev/SDV" target="_blank" rel="noopener noreferrer">GitHub</a>

- Gretel / YData - Tools to generate privacy-preserving financial crime datasets.

	- <a href="https://github.com/gretelai/gretel-synthetics" target="_blank" rel="noopener noreferrer">Gretel GitHub</a>
	
	- <a href="https://github.com/ydataai" target="_blank" rel="noopener noreferrer">YData GitHub</a>
	
- FCC-Synthetic-TM - Reproducible FCC synthetic data factory for transaction monitoring - customers, accounts, transactions, alerts, cases - ready for analytics & model testing.

	- <a href="https://github.com/SKR-35/FCC-Synthetic-TM" target="_blank" rel="noopener noreferrer">GitHub</a>
	
- Faker - Synthetic customer/KYC generation.

    - <a href="https://github.com/joke2k/faker" target="_blank" rel="noopener noreferrer">GitHub</a>

- Mimesis - Synthetic profile generation.

	- <a href="https://github.com/lk-geimfari/mimesis" target="_blank" rel="noopener noreferrer">GitHub</a>
  
- [openabm](https://github.com/ai-decisions/openabm) - Agent-based simulator of money-laundering networks with a pluggable detector for adversarial evaluation, Apache-2.0.	

## MLOps, Monitoring & Drift Detection

- MLflow - Model tracking, registry, experiment mgmt for financial crime models.

	- <a href="https://github.com/mlflow/mlflow" target="_blank" rel="noopener noreferrer">GitHub</a>

- Evidently AI - Data drift, concept drift, monitoring.

	- <a href="https://github.com/evidentlyai/evidently" target="_blank" rel="noopener noreferrer">GitHub</a>

- WhyLabs / whylogs - Data quality & model monitoring.

	- <a href="https://github.com/whylabs/whylogs" target="_blank" rel="noopener noreferrer">GitHub</a>
	
## Feature Engineering & Feature Store

- Featuretools - Automated feature engineering.

	- <a href="https://github.com/alteryx/featuretools" target="_blank" rel="noopener noreferrer">GitHub</a>
	
- Feast - Feature store for reusable financial crime features.

	- <a href="https://github.com/feast-dev/feast" target="_blank" rel="noopener noreferrer">GitHub</a>

## Explainability & Model Risk

- SHAP - Local/global explanations for financial crime models.

	- <a href="https://github.com/shap/shap" target="_blank" rel="noopener noreferrer">GitHub</a>
	
- LIME - Local explainability for suspicious activity scoring.

	- <a href="https://github.com/marcotcr/lime" target="_blank" rel="noopener noreferrer">GitHub</a>

- Fairlearn - Bias/fairness monitoring.

	- <a href="https://github.com/fairlearn/fairlearn" target="_blank" rel="noopener noreferrer">GitHub</a>

## Benchmarks & Datasets

- IEEE-CIS Fraud - Financial transactions fraud dataset (imbalanced).

	- <a href="https://www.kaggle.com/competitions/ieee-fraud-detection" target="_blank" rel="noopener noreferrer">Kaggle</a>

- Elliptic Bitcoin AML - Crypto AML labels for addresses/tx.

	- <a href="https://www.elliptic.co/media-center/elliptic-releases-bitcoin-transactions-data" target="_blank" rel="noopener noreferrer">Official Page</a>
	
	- <a href="https://www.kaggle.com/datasets/ellipticco/elliptic-data-set" target="_blank" rel="noopener noreferrer">Kaggle</a>
	
- PaySim - Mobile money fraud simulation dataset.

    - <a href="https://github.com/EdgarLopezPhD/PaySim" target="_blank" rel="noopener noreferrer">GitHub</a>

- IBM AML Simulated Transactions Dataset

	- <a href="https://github.com/IBM/AML-Data" target="_blank" rel="noopener noreferrer">GitHub</a>

	- <a href="https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml" target="_blank" rel="noopener noreferrer">Kaggle</a>
	
- Kaggle Credit Card Fraud Detection
  
	- <a href="https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud" target="_blank" rel="noopener noreferrer">Kaggle</a>

- [openlabels](https://github.com/ai-decisions/openlabels) / [openeval](https://github.com/ai-decisions/openeval) - Primary-source crypto address label tooling (OFAC SDN, 9 VASP registers, TagPack export) and an evaluation harness with lead-time replay against public designations, Apache-2.0.

## Certifications

### AML / Financial Crime

- ACAMS CAMS - Certified Anti-Money Laundering Specialist

    - https://www.acams.org

- ICA Advanced Certificate in Anti Money Laundering

    - https://www.int-comp.org

- ICA Diploma in Financial Crime Prevention

    - https://www.int-comp.org

### Fraud

- Certified Fraud Examiner (CFE)

    - https://www.acfe.com

### Sanctions

- Association of Certified Sanctions Specialists (ACSS)

    - https://sanctionsassociation.org/
	
- Certified Global Sanctions Specialist (CGSS)

	- https://www.acams.org/en/certifications/certified-global-sanctions-specialist-cgss

### Audit & Risk

- Certified Internal Auditor (CIA)

    - https://www.theiia.org

- Certified Information Systems Auditor (CISA)

    - https://www.isaca.org

- Financial Risk Manager (FRM)

    - https://www.garp.org

## Books

### Financial Crime & AML

- **The Laundrymen: Inside Money Laundering, the World's Third Largest Business**
  - Jeffrey Robinson

- **Money Laundering: A Guide for Criminal Investigators**
  - John Madinger

- **Dirty Entanglements: Corruption, Crime and Terrorism**
  - Louise I. Shelley

- **The World's Banker**
  - Sebastian Mallaby

### Fraud

- **Fraud Analytics Using Descriptive, Predictive and Social Network Techniques**
  - Bart Baesens

- **Financial Shenanigans**
  - Howard Schilit, Jeremy Perler, Yoni Engelhart

### Anti-Bribery & Corruption

- **The Foreign Corrupt Practices Act in a New Era**
  - Mike Koehler

### Sanctions & Compliance

- **Economic Sanctions: Theory and Practice**
  - Michael P. Malloy

### Investigations & Financial Intelligence

- **Financial Investigation and Forensic Accounting**
  - George A. Manning

- **Forensic Analytics: Methods and Techniques for Forensic Accounting Investigations**
  - Mark J. Nigrini

### Network & Criminal Organizations

- **Dark Commerce: How a New Illicit Economy Is Threatening Our Future**
  - Louise I. Shelley
  
## Documentaries, Movies & TV Series

Selected films, documentaries and series illustrating financial crime, fraud, corruption, market abuse, money laundering and investigative themes.

### Documentaries

- **Dirty Money** - Corporate fraud, corruption, financial misconduct and regulatory failures.
- **Enron: The Smartest Guys in the Room** - Accounting fraud, corporate governance failures and financial deception.
- **The Inventor: Out for Blood in Silicon Valley** - Corporate fraud, misrepresentation and governance failures surrounding Theranos.
- **The Tinder Swindler** - Romance fraud, social engineering and movement of victim funds.
- **The Panama Papers** - Offshore structures, shell companies, beneficial ownership and financial secrecy.

### Movies

- **The Wolf of Wall Street** - Securities fraud, market misconduct, financial crime and money laundering.
- **The Big Short** - Financial markets, conflicts of interest, misaligned incentives and systemic risk.
- **Margin Call** - Market risk, governance, conduct and decision-making during a financial crisis.
- **The Laundromat** - Offshore finance, shell companies, beneficial ownership and financial secrecy.
- **Boiler Room** - Securities fraud, high-pressure sales practices and market manipulation.

### TV Series

- **Ozark** - Money laundering, cash businesses, layering and organized crime.
- **Breaking Bad** - Laundering criminal proceeds through legitimate and cash-intensive businesses.
- **Better Call Saul** - Money laundering, front businesses organized crime and professional facilitation.
- **Billions** - Insider trading, market abuse, conflicts of interest and financial investigations.
- **McMafia** - Cross-border organized crime, money laundering, corruption and illicit financial networks.
  
## Typologies

Common financial crime and misconduct typologies relevant to detection, monitoring, investigation and risk assessment.

### Anti-Money Laundering (AML)

* **Structuring / Smurfing** - Breaking large transactions into smaller amounts to avoid reporting or monitoring thresholds.
* **Money Mule Activity** - Using individuals or accounts to receive, transfer or withdraw illicit funds on behalf of criminals.
* **Funnel Accounts** - Multiple geographically dispersed deposits followed by rapid withdrawal or transfer of funds elsewhere.
* **Pass-Through Accounts** - Accounts showing substantial incoming and outgoing activity while maintaining unusually low balances.
* **Round Tripping** - Funds transferred through multiple entities or jurisdictions before returning to their origin, obscuring ownership or source.
* **Shell Company Abuse** - Using entities with little or no genuine business activity to disguise ownership, transactions or movement of funds.
* **Trade-Based Money Laundering (TBML)** - Manipulating trade transactions, invoices, quantities, prices or documentation to transfer value.
* **Cash-Intensive Business Abuse** - Mixing illicit proceeds with apparently legitimate cash revenues.
* **Dormant Account Reactivation** - Previously inactive accounts suddenly exhibiting significant or unusual transaction activity.
* **Rapid Movement of Funds** - Funds entering an account and being transferred onward shortly afterwards with limited economic rationale.
* **Layering Through Multiple Accounts** - Moving funds through chains of accounts, entities, products or jurisdictions to obscure their origin.
* **Money Laundering Through Virtual Assets** - Using cryptoassets, exchanges, mixers, bridges or multiple wallets to obscure transaction trails.

### Fraud

* **Account Takeover (ATO)** - Unauthorized control of an existing account using compromised credentials or social engineering.
* **Authorized Push Payment (APP) Fraud** - Manipulating victims into authorizing payments to accounts controlled by fraudsters.
* **Synthetic Identity Fraud** - Combining real and fabricated identity information to create apparently legitimate customers.
* **First-Party Fraud** - Customers intentionally misrepresenting information or disputing legitimate transactions for financial gain.
* **Identity Theft** - Using another person's identity or credentials to obtain funds, credit, goods or services.
* **Card-Not-Present Fraud** - Fraudulent transactions conducted without physical presentation of the payment card.
* **Invoice / Payment Diversion Fraud** - Manipulating invoices or payment instructions so legitimate payments are redirected.
* **Romance and Investment Scams** - Building trust with victims before inducing payments or fraudulent investments.
* **Merchant Fraud** - Abuse involving fraudulent merchants, transaction laundering, collusion or deceptive commercial activity.
* **Bust-Out Fraud** - Establishing apparently legitimate credit behavior before rapidly maximizing available credit and abandoning repayment obligations.

### Anti-Bribery & Corruption (AB&C)

* **Kickbacks** - Returning part of a payment or contract value to an individual who influenced the underlying decision.
* **Bribery Through Intermediaries** - Using agents, consultants, distributors or other third parties to conceal improper payments.
* **Improper Gifts & Hospitality** - Providing excessive gifts, travel, entertainment or hospitality to improperly influence decisions.
* **Procurement Corruption** - Manipulating tendering, vendor selection, pricing or contracting processes for improper benefit.
* **Conflict of Interest** - Undisclosed personal or financial interests influencing professional or commercial decisions.
* **Fictitious Vendors** - Creating or using false suppliers to divert corporate or public funds.
* **Charitable Donation Abuse** - Using donations or sponsorships as indirect mechanisms for transferring improper benefits.
* **Facilitation Payments** - Payments intended to expedite routine governmental or administrative actions.
* **Political Contribution Abuse** - Using political donations or related payments to obtain improper business or regulatory advantages.

### Trade Surveillance / Market Abuse

* **Insider Dealing** - Trading or encouraging trading while possessing material non-public information.
* **Spoofing** - Placing orders without genuine execution intent to create a misleading impression of supply or demand.
* **Layering** - Placing multiple non-bona-fide orders at different price levels to influence market perception or execution.
* **Wash Trading** - Trading without meaningful change in beneficial ownership to create artificial activity or volume.
* **Pump and Dump** - Artificially promoting or inflating an asset's price before selling accumulated positions.
* **Marking the Close** - Trading near market close to influence closing prices or valuation benchmarks.
* **Front Running** - Trading ahead of known client or institutional orders to benefit from the expected price movement.
* **Cross-Market Manipulation** - Using activity in one instrument, venue or market to manipulate the price of another.
* **Collusive Trading** - Coordinated trading between participants intended to manipulate price, volume, liquidity or market perception.
* **Benchmark Manipulation** - Attempting to influence prices, submissions or transactions used to calculate financial benchmarks.

### E-Comms / Conduct Surveillance

* **Collusion Indicators** - Communications suggesting coordination between employees, traders, counterparties or competitors.
* **Information Leakage** - Unauthorized disclosure of confidential, client, transaction or material non-public information.
* **Off-Channel Communications** - Conducting business through unapproved messaging platforms, personal devices or communication channels.
* **Code Words / Euphemisms** - Using disguised language intended to conceal potentially improper conduct.
* **Pressure or Coercion** - Communications indicating attempts to improperly influence colleagues, clients, counterparties or decision-makers.
* **Intent to Circumvent Controls** - Discussions about avoiding surveillance, approvals, reporting requirements or internal controls.
* **Inappropriate Information Sharing** - Sharing restricted information across information barriers or with unauthorized recipients.
* **Communication-Trading Correlation** - Suspicious communications occurring shortly before or during potentially abusive trading activity.

### Sanctions Evasion

* **Intermediary / Front Company Use** - Routing transactions through third parties or companies to conceal involvement of sanctioned parties.
* **Ownership and Control Obfuscation** - Using complex ownership structures to hide sanctioned beneficial owners or controllers.
* **Payment Routing Through Third Countries** - Routing payments through jurisdictions or institutions intended to obscure sanctioned exposure.
* **Vessel Identity Manipulation** - Changing vessel names, flags, ownership, registration or identification information.
* **AIS Manipulation / Dark Activity** - Disabling or manipulating vessel tracking systems to conceal movements or transfers.
* **Transshipment and Origin Concealment** - Moving goods through intermediary jurisdictions to disguise their true origin or destination.
* **Invoice and Documentation Manipulation** - Altering trade documentation to hide sanctioned goods, entities, jurisdictions or counterparties.
* **Virtual Asset Sanctions Evasion** - Using cryptoassets, multiple wallets, mixers or decentralized services to circumvent restrictions.

### KYC / Customer Risk

* **Beneficial Ownership Concealment** - Using layered legal entities, nominees, trusts or intermediaries to obscure ultimate ownership.
* **Nominee Directors / Shareholders** - Using individuals who formally hold positions or ownership on behalf of undisclosed controllers.
* **False or Synthetic Identity** - Providing fabricated, altered, stolen or combined identity information during onboarding.
* **Address / Contact Reuse** - Multiple apparently unrelated customers sharing addresses, phone numbers, emails, devices or other identifiers.
* **Unexplained High-Risk Jurisdiction Exposure** - Customer relationships or activity involving higher-risk jurisdictions without credible rationale.
* **Business Profile Mismatch** - Customer transactions materially inconsistent with declared occupation, business model, expected activity or source of funds.
* **Rapid Changes in Ownership or Control** - Frequent or unexplained changes to shareholders, directors, beneficial owners or corporate structure.

## Regulations, Standards & Guidance

### Global AML / CFT

- FATF Recommendations - Global standards for combating money laundering, terrorist financing and proliferation financing.

	- <a href="https://www.fatf-gafi.org/en/topics/fatf-recommendations.html" target="_blank" rel="noopener noreferrer">Official Page</a>

- FATF Risk-Based Approach Guidance - Guidance and resources for applying risk-based AML/CFT supervision and controls.

	- <a href="https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-supervision.html" target="_blank" rel="noopener noreferrer">Official Page</a>

- Basel Committee - Sound Management of Risks Related to Money Laundering and Financing of Terrorism - Banking-sector guidance on AML/CFT governance and risk management.

    - <a href="https://www.bis.org/bcbs/publ/d505.htm" target="_blank" rel="noopener noreferrer">Official Page</a>

- EU Anti-Money Laundering Framework / AMLA - European AML/CFT regulatory framework and the EU Anti-Money Laundering Authority.

    - <a href="https://finance.ec.europa.eu/financial-crime/anti-money-laundering-and-countering-financing-terrorism-eu-level_en" target="_blank" rel="noopener noreferrer">European Commission</a>

    - <a href="https://www.amla.europa.eu/index_en" target="_blank" rel="noopener noreferrer">AMLA</a>

### Banking & Industry Guidance

- Wolfsberg Group - Industry principles and guidance for financial crime risk management.

    - <a href="https://wolfsberg-group.org/" target="_blank" rel="noopener noreferrer">Official Page</a>

- Wolfsberg Group Resources - Practical guidance and standards for financial crime risk management professionals.

    - <a href="https://wolfsberg-group.org/resources" target="_blank" rel="noopener noreferrer">Wolfsberg Resources</a>
	
- BIS papers

	- <a href="https://www.bis.org/bispapers/index.htm" target="_blank" rel="noopener noreferrer">Official Page</a>

### Sanctions

- OFAC Sanctions Programs and Guidance - Official U.S. sanctions information, compliance resources and program guidance.

    - <a href="https://ofac.treasury.gov/" target="_blank" rel="noopener noreferrer">Official Page</a>

### Market Abuse

- EU Market Abuse Regulation (MAR) - European regulatory framework addressing insider dealing, unlawful disclosure of inside information and market manipulation.

    - <a href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0596" target="_blank" rel="noopener noreferrer">EUR-Lex</a>

- FCA Market Abuse Guidance - UK regulatory guidance and resources concerning market abuse.

    - <a href="https://www.fca.org.uk/markets/market-abuse" target="_blank" rel="noopener noreferrer">Official Page</a>

### Anti-Bribery & Corruption

- UK Bribery Act 2010 Guidance - Official guidance for commercial organizations on procedures designed to prevent bribery.

    - <a href="https://www.gov.uk/government/publications/bribery-act-2010-guidance" target="_blank" rel="noopener noreferrer">Official Page</a>

- DOJ / SEC FCPA Resource Guide - Detailed guidance on the U.S. Foreign Corrupt Practices Act, enforcement principles and corporate compliance expectations.

    - <a href="https://www.justice.gov/criminal/criminal-fraud/fcpa-resource-guide" target="_blank" rel="noopener noreferrer">DOJ Official Page</a>

- United Nations Convention against Corruption (UNCAC) - International framework covering corruption prevention, criminalization, international cooperation and asset recovery.

    - <a href="https://www.unodc.org/unodc/en/corruption/uncac.html" target="_blank" rel="noopener noreferrer">UNODC Official Page</a>

### Financial Intelligence

- FinCEN Advisories - Official advisories addressing financial crime threats, typologies and suspicious financial activity.

    - <a href="https://www.fincen.gov/resources/advisoriesbulletinsfact-sheets/advisories" target="_blank" rel="noopener noreferrer">Official Page</a>

- Egmont Group - International cooperation, standards and knowledge resources for Financial Intelligence Units (FIUs).

    - <a href="https://egmontgroup.org/" target="_blank" rel="noopener noreferrer">Official Page</a>

- Egmont Group Core Documents - Principles and operational guidance supporting cooperation and information exchange between FIUs.

    - <a href="https://egmontgroup.org/resource_type/core-documents/" target="_blank" rel="noopener noreferrer">Core Documents</a>
