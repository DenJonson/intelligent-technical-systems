import git


with open("url.txt") as source:
    gitUrl = source.readlines()
    
result={}
gitUrl=[url.rstrip() for url in gitUrl]

for i in range(len(gitUrl)):
    try:
        folder = gitUrl[i].split('/')[-1] + "-https"
        git.Repo.clone_from(gitUrl[i], folder)
        result[gitUrl[i]] = 'OK'
    except:
        result[gitUrl[i]]='FAIL'
        
with open("results.txt", "w") as resultFile:
    for url in gitUrl:
        resultFile.write(f"{url}\t")
        resultFile.write(f"{result[url]}\n")