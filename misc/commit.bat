set /p "msg=Commit Message: "

git add -A
git commit -m "%msg%"
git push

cls