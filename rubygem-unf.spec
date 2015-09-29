Name     : rubygem-unf
Version  : 0.1.4
Release  : 6
URL      : https://rubygems.org/downloads/unf-0.1.4.gem
Source0  : https://rubygems.org/downloads/unf-0.1.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : ruby
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-bundler
BuildRequires : rubygem-i18n
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-shoulda
BuildRequires : rubygem-shoulda-context
BuildRequires : rubygem-shoulda-matchers
BuildRequires : rubygem-test-unit
BuildRequires : rubygem-thread_safe
BuildRequires : rubygem-tzinfo
BuildRequires : rubygem-unf_ext

%description
ruby-unf
========
Synopsis
--------
* A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n unf-0.1.4
gem spec %{SOURCE0} -l --ruby > rubygem-unf.gemspec

%build
gem build rubygem-unf.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
unf-0.1.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/unf-0.1.4 
sed -i.orig \
    -e '/begin/,/end/d' \
    -e '/bundler/d' \
    test/helper.rb
    
    sed -i.minitest \
        -e 's|Test::Unit::TestCase|Minitest::Test|' \
        test/*.rb
cat > test/unit.rb << EOF
gem "minitest"
require "minitest/autorun"
EOF

ruby -I.:lib:test test/test_unf.rb
popd

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/unf-0.1.4.gem
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/String/to_nfc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/String/to_nfd-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/String/to_nfkc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/String/to_nfkd-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/UNF/Normalizer/cdesc-Normalizer.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/UNF/Normalizer/instance-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/UNF/Normalizer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/UNF/Normalizer/normalize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/UNF/Normalizer/normalize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/UNF/cdesc-UNF.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/page-LICENSE.ri
/usr/lib64/ruby/gems/2.2.0/doc/unf-0.1.4/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/README.md
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/lib/unf.rb
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/lib/unf/normalizer.rb
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/lib/unf/normalizer_cruby.rb
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/lib/unf/normalizer_jruby.rb
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/lib/unf/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/test/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/test/helper.rb.minitest
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/test/helper.rb.orig
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/test/normalization-test.txt
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/test/test_unf.rb
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/test/test_unf.rb.minitest
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/test/unit.rb
/usr/lib64/ruby/gems/2.2.0/gems/unf-0.1.4/unf.gemspec
/usr/lib64/ruby/gems/2.2.0/specifications/unf-0.1.4.gemspec
