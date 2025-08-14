docker build -f Dockerfile -t testAPI .
docker run -p 8000:8000 testAPI
# In neuem Terminal:
curl localhost:8000