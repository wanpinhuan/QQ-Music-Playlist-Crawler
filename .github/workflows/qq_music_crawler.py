name: QQ Music Playlist Crawler
 
on:
  schedule:
'0 0 * * *' # 每天午夜运行
 
jobs:
  crawl:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
 
      - name: Setup Python
        uses: actions/setup-python@v2
        with
3.8
 
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
txt
      - name: Crawl QQ Music Playlists
        env:
{{}}
{{}}
        run: |
py
      - name: Upload Artifacts
        uses: actions/upload-artifact@v2
        with
          name: playlists
          path: playlists
