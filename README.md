A tool to scrape any website using playwright and let an llm do things with it. **ULTIMATE SLOP**. Just give the url and ask the llm to do anything with the data on that website. Make it roast something like github roaster or twitter roaster, make it summarize it or tell it to organize the data you want from the specific website.

Just add the url and ask anything.

### Installing
1. Installing dependencies
```
$ pip install -r requirements.txt
```

2. Installing the model. Im using llama3.1:8B but you can just change the llm model in llmin.py and use any model of your choice.
- Install Ollama. Go to this website for installation for mac and windows: [Ollama](https://ollama.com/download/mac)
```
$ curl -fsSL https://ollama.com/install.sh | sh // linux
```

- Install the model
```
$ ollama run llama3.1:latest
```

3. Running the website
```
$ streamlit run main.py
```

### Usage
1. go to any website and grab the url.
2. Put the url in the text area.
3. click on scrape website. it will scrape the websites data and give you the dom content.
4. Prompt the llm in the text area on what do you wanna do with the stuff on the webpage and click on parse content.
4. Wait for some time and voila.


- i'll change this from using a local model to using api like free llm api's. it should take like 10 mins.
