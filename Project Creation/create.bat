@echo off

cd /d D:\Projects
if exist %1 (
    echo ...................................
    echo %1 folder already exist!!! 
    echo Try using a different project name.
    echo ...................................
    ) else (
        md %1
        cd %1
        "C:\Users\cypherphage\AppData\Local\Programs\Python\Python37-32\python.exe" "C:\Scripts\create.py" "%1"
        if exist success.txt (
            echo "# %1" > README.md
            git init 
            git add README.md
            git commit -m "first commit"
            git remote add origin https://github.com/adityanain96/%1.git
            git push -u origin master
            code .
            cd ..
            ) else (
                echo ....................................
                echo %1 repository already exist!!!. 
                echo Try using a different project name.
                echo ....................................
                )
        pause
        )


