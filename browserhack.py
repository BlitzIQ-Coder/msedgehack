import subprocess
import time
#for i in range(2):
    #print(f"Iteration {i + 1} of 5")
    #time.sleep(2)

#list
search_terms = [
    "artificial intelligence",
    "machine learning",
    "data science",
    "cloud computing",
    "cybersecurity",
    "blockchain technology",
    "internet of things",
    "augmented reality",
    "virtual reality",
    "big data analytics",
    "quantum computing",
    "5G technology",
    "cryptocurrency",
    "smart cities",
    "autonomous vehicles",
    "natural language processing",
    "edge computing",
    "deep learning",
    "bioinformatics",
    "genomics",
    "digital transformation",
    "robotics",
    "renewable energy",
    "sustainable technology",
    "nanotechnology",
    "wearable technology",
    "mobile app development",
    "e-commerce trends",
    "digital marketing",
    "fintech innovations"
]

for terms in search_terms:
    url=f"https://www.bing.com/search?q={terms}"
    subprocess.Popen(["start", "msedge",url], shell=True) 
    time.sleep(5)  


#subprocess.Popen(["taskkill", "/IM", "msedge.exe", "/F"], shell=True)
time.sleep(2)

    #test 002 reopen edge
    #subprocess.Popen(["start", "msedge","https://www.bing.com/search?q=car"], shell=True)
input("process completed, press enter to exit")
