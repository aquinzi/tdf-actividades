# Fixes SSL Connection Error in Windows execution of Ruby
# Based on fix described at: https://gist.github.com/fnichol/867550
ENV['SSL_CERT_FILE'] = File.expand_path(File.dirname(__FILE__)) + "/cacert.pem"

source 'https://rubygems.org'

require "json"
require "open-uri"
#get versions specific to github
versions = JSON.parse(open("https://pages.github.com/versions.json").read)

gem "jekyll", versions["jekyll"], group: :jekyll_plugins
gem "jekyll-sass-converter", versions["jekyll-sass-converter"], group: :jekyll_plugins
#gem "jekyll-textile-converter", versions["jekyll-textile-converter"], group: :jekyll_plugins
gem "kramdown", versions["kramdown"], group: :jekyll_plugins
#gem "redcarpet", versions["redcarpet"], group: :jekyll_plugins
#gem "RedCloth", versions["RedCloth"], group: :jekyll_plugins
gem "liquid", versions["liquid"], group: :jekyll_plugins
gem "rouge", versions["rouge"], group: :jekyll_plugins
#gem "github-pages-health-check", versions["github-pages-health-check"], group: :jekyll_plugins
gem "jemoji", versions["jemoji"], group: :jekyll_plugins
gem "jekyll-mentions", versions["jekyll-mentions"], group: :jekyll_plugins
gem "jekyll-redirect-from", versions["jekyll-redirect-from"], group: :jekyll_plugins
gem "jekyll-sitemap", versions["jekyll-sitemap"], group: :jekyll_plugins
#gem "jekyll-feed", versions["jekyll-feed"], group: :jekyll_plugins
gem "jekyll-gist", versions["jekyll-gist"], group: :jekyll_plugins
gem "jekyll-paginate", versions["jekyll-paginate"], group: :jekyll_plugins
gem "jekyll-coffeescript", versions["jekyll-coffeescript"], group: :jekyll_plugins
gem "jekyll-seo-tag", versions["jekyll-seo-tag"], group: :jekyll_plugins
gem "jekyll-github-metadata", versions["jekyll-github-metadata"], group: :jekyll_plugins
gem "listen", versions["listen"], group: :jekyll_plugins
#gem "github-pages", versions["github-pages"], group: :jekyll_plugins
gem "html-pipeline", versions["html-pipeline"], group: :jekyll_plugins
gem "sass", versions["sass"], group: :jekyll_plugins
gem "safe_yaml", versions["safe_yaml"], group: :jekyll_plugins
gem 'wdm', '>= 0.1.0' if Gem.win_platform? #ruby kindly asked for it