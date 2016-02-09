 # Fixes SSL Connection Error in Windows execution of Ruby
 # Based on fix described at: https://gist.github.com/fnichol/867550
 ENV['SSL_CERT_FILE'] = File.expand_path(File.dirname(__FILE__)) + "/cacert.pem"

source 'https://rubygems.org'

require "json"
require "open-uri"
#get versions specific to github
versions = JSON.parse(open("https://pages.github.com/versions.json").read)

gem "jekyll", versions["jekyll"]
gem "jekyll-coffeescript", versions["jekyll-coffeescript"]
gem "jekyll-sass-converter", versions["jekyll-sass-converter"]
gem "kramdown", versions["kramdown"]
#gem "maruku", versions["maruku"]
#gem "rdiscount", versions["rdiscount"] #we cant install it in windows
#gem "redcarpet", versions["redcarpet"] #no support in GH pages
#gem "pygments.rb", versions["pygments.rb"]
gem "rouge", versions["rouge"] #for code highlighting
#gem "RedCloth", versions["RedCloth"] #tetxtile, no support in GH pages
gem "liquid", versions["liquid"]
gem "jemoji", versions["jemoji"]
gem "jekyll-mentions", versions["jekyll-mentions"]
gem "jekyll-redirect-from", versions["jekyll-redirect-from"]
gem "jekyll-sitemap", versions["jekyll-sitemap"]
gem "jekyll-feed", versions["jekyll-feed"]
gem "jekyll-seo-tag", versions["jekyll-seo-tag"]
#gem "ruby", versions["ruby"] #avoid problems in windows
gem "github-pages", versions["github-pages"]
gem "html-pipeline", versions["html-pipeline"]
gem "sass", versions["sass"]
gem "safe_yaml", versions["safe_yaml"]
gem 'wdm', '>= 0.1.0' if Gem.win_platform? #ruby kindly asked for it