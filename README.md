# ProcessFlow: Your Local & Private GPT :dependabot:

⚡ Your personal & private chatbot running on open LLM model(s) ⚡

[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/kunalsuri)](https://twitter.com/kunalsuri)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub language count](https://img.shields.io/github/languages/count/kunalsuri/ProcessFlowGPT)
![GitHub top language](https://img.shields.io/github/languages/top/kunalsuri/ProcessFlowGPT?color=yellow)
![GitHub Repo stars](https://img.shields.io/github/stars/kunalsuri/ProcessFlowGPT)



<br>
> Author: Kunal Suri, Ph.D.
<br>

## 🚀 How to use ProcessFlowGPT?
This application will can be executed on your local machine using open-source LLM models via the Ollama framework

### Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Running ProcessFlowGPT Locally via CLI](#Running-ProcessFlowGPT-Locally-CLI)

<br>

---

### Prerequisites

The ProcessFlowGPT App runs on your local machine via Ollama framework. To use this app, you need do the following steps:

1. **Download, Install and Run Ollama Application**

   > The Ollama framework enables easy interaction between your chatbot and the LLM models from the convenience of your local machine.
   
   Kindly, follow the instructions from [Ollama](https://ollama.com/) website to download and install the framework in your local machine. Once Ollama is installed, you can run a local open-source LLM model from your machine. The general steps are given below:

   > (For more details and info please check: website: [Ollama](https://ollama.com/)) || **GitHub:** https://github.com/ollama/ollama

<div align="center">
  <img alt="ollama" height="200px" src="https://github.com/ollama/ollama/assets/3325447/0d0b44e2-8f4a-4e99-9b52-a5c1c741c8f7">
</div>

   - Download and Install Ollama app (Supported Platforms: Windows, Linux, MacOS)
      
      - For Window Users: Once Ollama application is downloaded, you will need to run the Ollama app from Programs
      
      - Once the Ollama app is running, go to commant prompt (CLI) and type:
        
        ```bash
           Ollama list
        ```
        > Note: This command is used to list all the open-source LLM models available in your system locally. However, on the first run, then may be no LLM models in your system.

    
   - To download the LLM model, run the command
     >  Ollama run <Model_Name>
     
       ```bash
          ollama run mistral:7b
       ```
     
     > This command will check if the model is available in the local repo on your machine, if not then it will fetch the LLM model from Ollama Website and then start running it.

   
2. **Replicate the Git Repo in your local machine**

   > We assume that you have cloned the ProcessFlowGPT repo on your local machine. If not, do the following:

```bash
git clone https://github.com/kunalsuri/ProcessFlowGPT.git
```

<br>

⚠️ Recommendation: To keep their python installations for other projects clean, we recommend that the users create a new python virtual environment for the ProcessFlowGPT project and install the python packages via requirement.txt (in Step 3 below)

<br>

3. **Install the python packages needed to run the ProcessFlowGPT Chatbot**

> ProcessFlowGPT.py application needs the following packages: ollama, streamlit. They have been included to the requirements.txt and can be easily installed. To install the packages, go to the folder containing ProcessFlowGPT and enter the below command:

```bash
pip install -r requirements.txt
```

<br>

---

### Running ProcessFlowGPT Locally via CLI
ProcessFlowGPT uses open-source LLM models running on your machine via the **Ollama** framework. To run these models, the user needs to install Ollama (as detailed in the Prerequisite section above). 

We assume that you have installed the Ollama framework and downloaded the open LLM models such as [Mistral](https://mistral.ai/technology/#models), or Meta's [Llama](https://llama.com/), to name just a few.

> To run the ProcessFlowGPT via command-line interface (CLI) use the following command: 

```bash
streamlit run process-flow-gpt.py
```

✅ Once executed, the ProcessFlowGPT Chatbot will start running on your web browser and will be ready for your use.

<br>

---

## Further Reading on Llama | Meta
- [Llama website](https://www.llama.com/) 

## 🛡️Responsible AI 
:european_union: **EU's Guidelines on the responsible use of generative AI in research:** https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/guidelines-responsible-use-generative-ai-research-developed-european-research-area-forum-2024-03-20_en

<br>

⚠️ Note: In no circumstance shall the author(s) or copyright holder(s) be held liable for any claim, damages, or other liabilities arising from the utilization of this code, which incorporates several code snippets generated by artificial intelligence (AI), along with open-source contributions from other programmers sourced from platforms including GitHub and other, pursuant to the terms outlined in the MIT License.
