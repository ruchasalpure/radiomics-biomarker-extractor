from crewai import Agent

radiomics_biomarker_extractor = Agent(
    role="Radiomics Biomarker Extractor",
    goal="Deliver high-precision autonomous Radiomics Biomarker Extractor operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
