### Quick URL hacks

- To list all spiders: http://localhost:8000/scrape/_spiders

- To list all jobs: http://localhost:8000/scrape/_jobs

- To list all items: http://localhost:8000/scrape/_items

- To list dumps from one of the spiders: http://localhost:8000/scrape/_items/SPIDER_NAME

- To render one of the spiders in JSON format, note the name of the dump from previous command and use it in following URL: 
     
     http://localhost:8000/scrape/render/SPIDER_NAME/JOB_ID


  *  Example: http://localhost:8000/scrape/render/HBR/d3fdf38a02ae11e4a118dc85de32e017

  *  The job id and name could be checked from /scrape/_jobs URL
