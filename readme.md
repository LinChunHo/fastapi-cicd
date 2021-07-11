## for github
echo "# fastapi-cicd" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/LinChunHo/fastapi-cicd.git
git push -u origin master

## for docker

docker push lincheric/fastapi-cicd:v1


Copy Access Token
When logging in from your Docker CLI client, use this token as a password. Learn more
ACCESS TOKEN DESCRIPTION
nancy0622
To use the access token from your Docker CLI client:
1. Run docker login --username lincheric
2. At the password prompt, enter the personal access token.
e13f61f1-c1c0-4ddc-9ba8-e66846edecb6
WARNING: This access token will only be displayed once. It will not be stored and cannot be retrieved. Please be sure to save it now.

==================


# This is a basic workflow to help you get started with Actions

name: CI to Docker Hub

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the master branch
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - name: Check out Repo
      - uses: actions/checkout@v2

      # Runs a single command using the runners shell
      - name: login to docker hub
        uses: docker/login-action@v1
        with:
          username:${{ secrets.DOCKER_HUB_USERNAME }}
          password:${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}
          
      - name: Setup docker buildx
        id: buildx
        uses: docker/setup-buildx-action@v2
        with:
          context: ./
          file: ./Dockerfile
          push: true
          tags: ${{ secrets.DOCKER_HUB_USERNAME }}/fastapi-cicd:latest

      - name: Image digest
        run: echo ${{ steps.docker_build.outputs.digest }}