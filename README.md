# fcwps-project1

풀스택 개발 취업완성 스쿨(Python)의 Python Mini Project repository.

## How to contribute?

1. 이 repo에서 issue를 생성합니다.
2. 제목과 내용은 자유롭게 작성하되, 내용에는 진행할 주제를 작성해야 합니다.
3. repo를 fork, clone 합니다.
4. `$ git flow init`
5. On develop branch, `$ git flow feature start {FeatureName}`
    - 본인의 username으로 directory를 생성.
6. Do some work. (마지막 commit의 메시지내용은 resolved: #{issuenumber})
7. After work, `$ git push -u origin feature/{FeatureName}`
8. `$ git flow feature finish {FeatureName}`
9. `$ git push origin develop`
10. fork한 자신의 repo에서 `Create pull request`
11. base: ulgoon/develop compare: {username}/develop
12. wait for merge.
