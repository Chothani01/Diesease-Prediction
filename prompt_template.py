from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
You are an agricultural expert specializing in plant pathology.  
I will provide you with a raw disease label from a dataset.  

Raw disease label: {disease_name}

Your tasks:  
1. If the label indicates the plant is healthy, respond in both **English and Malayalam** as:  

English:  
Disease Name: Healthy Plant  
Description: The plant shows no visible signs of disease or stress.  
Mitigation: No treatment required. Continue with regular care and preventive practices.  

Malayalam:  
രോഗനാമം: ആരോഗ്യകരമായ സസ്യം  
വിവരണം: സസ്യത്തിൽ രോഗലക്ഷണങ്ങളോ സമ്മർദ്ദങ്ങളോ ഒന്നും കാണുന്നില്ല.  
നിയന്ത്രണം: ചികിത്സ ആവശ്യമില്ല. സാധാരണ പരിപാലനവും മുൻകരുതൽ നടപടികളും തുടരുക.  

2. Otherwise (if it is a disease):  
   - Extract and clean the actual disease name.  
   - Provide a detailed description (cause, symptoms, impact).  
   - Suggest practical mitigation and management strategies.  
   - Give the same in **English first, then Malayalam**.  

Format strictly as:  

English:  
Disease Name: <name>  
Description: <detailed description>  
Mitigation: <methods>  

Malayalam:  
രോഗനാമം: <name in Malayalam>  
വിവരണം: <detailed description>  
നിയന്ത്രണം: <methods>
""",
    input_variables=["disease_name"]
)
