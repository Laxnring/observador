# observador

Since the ["Observador"](https://observador.pt/) news outlet doesn't implement proper verification while using its api to fetch articles, this Python snippet uses it to generate a page similar to the outlet's landing page. 
The api call has been reverse-engineered using the Fiddler Tool with an iOS device and is repeated by the python script to fetch all the main articles on display. This bypasses the "premium" detection (these articles can only be read by paid subscribers or free users with premium articles left in the current month). It downloads them to the working directory of the script and creates an index.html file for easier navigation through the articles. Using a simple Python webserver it can quickly 
# Run:
`python ./observador.py`
Spinning a simple HTTP server using twistd example:
`twistd -n web --path="./observador"`
If you're reading this, Observador, please change your api calls to control whether a user still has free premium articles left this month.
