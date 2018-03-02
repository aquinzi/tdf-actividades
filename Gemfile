# Fixes SSL Connection Error in Windows execution of Ruby
# Based on fix described at: https://gist.github.com/fnichol/867550
ENV['SSL_CERT_FILE'] = File.expand_path(File.dirname(__FILE__)) + "/cacert.pem"

source 'https://rubygems.org'

#require "json"
#require "open-uri"
#get versions specific to github
#versions = JSON.parse(open("https://pages.github.com/versions.json").read)

gem "jekyll", "3.6.2", group: :jekyll_plugins
#gem "jekyll-sass-converter", "1.5.0", group: :jekyll_plugins
#gem "jekyll-textile-converter", versions["jekyll-textile-converter"], group: :jekyll_plugins
gem "kramdown", "1.14", group: :jekyll_plugins
#gem "redcarpet", versions["redcarpet"], group: :jekyll_plugins
#gem "RedCloth", versions["RedCloth"], group: :jekyll_plugins
gem "liquid", "4.0.0", group: :jekyll_plugins
gem "rouge", "1.11.1", group: :jekyll_plugins
#gem "github-pages-health-check", versions["github-pages-health-check"], group: :jekyll_plugins
#gem "jemoji", versions["jemoji"], group: :jekyll_plugins
#gem "jekyll-mentions", versions["jekyll-mentions"], group: :jekyll_plugins
gem "jekyll-redirect-from", "0.12.1", group: :jekyll_plugins
gem "jekyll-sitemap", "1.1.1", group: :jekyll_plugins
#gem "jekyll-feed", versions["jekyll-feed"], group: :jekyll_plugins
#gem "jekyll-gist", versions["jekyll-gist"], group: :jekyll_plugins
#gem "jekyll-paginate", versions["jekyll-paginate"], group: :jekyll_plugins
#gem "jekyll-coffeescript", versions["jekyll-coffeescript"], group: :jekyll_plugins
#gem "jekyll-seo-tag", versions["jekyll-seo-tag"], group: :jekyll_plugins
gem "jekyll-github-metadata", "2.9.3", group: :jekyll_plugins
gem "listen", "3.0.6", group: :jekyll_plugins
#gem "github-pages", versions["github-pages"], group: :jekyll_plugins
#gem "html-pipeline", versions["html-pipeline"], group: :jekyll_plugins
#gem "sass", versions["sass"], group: :jekyll_plugins
gem "safe_yaml", "1.0.4", group: :jekyll_plugins
gem 'wdm', '>= 0.1.0' if Gem.win_platform? #ruby kindly asked for it

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw]