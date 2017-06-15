## How to use

Install golang.  Follow the installation instructions for [Cloudflare's log CLI tool](https://github.com/cloudflare/logshare).  Follow its instructions for querying your logs and then pipe the output of the file to els_mangle.

els_mangle will munge the data such that it outputs data in this format:

```csv
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:53.0) Gecko/20100101 Firefox/53.0,Mac OSX 10.10,desktop,Firefox,53.0
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",Mac OSX 10.10.5,desktop,Chrome,58.0.3029.110
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.2.5 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.5",Mac OSX 10.10.5,desktop,Safari,10.1.1
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4",iPhone 10.3.2,mobile,Firefox,7.5
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) CriOS/59.0.3071.84 Mobile/14F89 Safari/602.1",iPhone 10.3.2,mobile,Chrome,59.0.3071.84
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 Mobile/14F89 Safari/602.1",iPhone 10.3.2,mobile,Safari,10.0
```

Info on the expect JSON input format can be found [here](https://support.cloudflare.com/hc/en-us/article_attachments/205413947/els_schema.json).