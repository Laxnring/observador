# observador

Since the ["Observador"](https://observador.pt/) news outlet doesn't implement proper verification while using its api to fetch articles, this Python snippet uses it to generate a page similar to the outlet's landing page. 

The api call has been reverse-engineered using the Fiddler Tool with an iOS device and is repeated by the python script to fetch all the main articles on display. This bypasses the "premium" detection (these articles can only be read by paid subscribers or free users with premium articles left in the current month). It downloads them to the working directory of the script and creates an index.html file for easier navigation through the articles. Using a simple Python webserver it can quickly 
# Run:
`python ./observador.py`

Spinning a simple HTTP server using twistd example:
`twistd -n web --path="./observador"`

# Disclaimer
I'm not in any way affiliated with Observador, nor do I have any nefarious intent. This small project is intended to highlight a critical flaw in the design of the platform which may affect the outlet's business model. Therefore, and in defense of free speech and the maintenance of one of the most respected Portuguese news outlets, I would want them to fix this flaw in their code. 

