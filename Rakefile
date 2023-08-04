require 'html-proofer'

task :html_proofer do
  build_dir = File.join(File.dirname(__FILE__), '_site')
  unless File.directory?('test/_site')
    `jekyll build -d #{build_dir} -V`
  end
  opts = {
    url_ignore: [/localhost/],
    empty_alt_ignore: true,
    file_ignore: [/slides/],
    typhoeus: {
      ssl_verifyhost: 0,
      ssl_verifypeer: false,
      timeout: 30
    }
  }
  HTMLProofer.check_directory(build_dir, opts).run
end