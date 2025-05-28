#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Remove toctrees from Sphinx pages
Summary(pl.UTF-8):	Usuwanie drzew ze spisem treści ze stron Sphinksa
Name:		python3-sphinx_remove_toctrees
Version:	1.0.0.post1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_remove_toctrees/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_remove_toctrees/sphinx_remove_toctrees-%{version}.tar.gz
# Source0-md5:	a348043f08b63f73a767206e2ced0c9d
URL:		https://pypi.org/project/sphinx_remove_toctrees/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6
%if %{with tests}
BuildRequires:	python3-Sphinx >= 4.5
BuildRequires:	python3-ipython
BuildRequires:	python3-myst_parser
BuildRequires:	python3-pytest
BuildRequires:	python3-sphinx_book_theme
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-ipython
BuildRequires:	python3-myst_parser
BuildRequires:	python3-sphinx_book_theme
BuildRequires:	sphinx-pdg-3 >= 4.5
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Improve your Sphinx build time by selectively removing TocTree objects
from pages. This is useful if your documentation uses auto-generated
API documentation, which generates a lot of stub pages.

This extension can be used to remove the sidebar links for just the
pages you specify, speed up the build considerably.

%description -l pl.UTF-8
Poprawa czasu budowania dokumentacji Sphinksem poprzez wybiórcze
usuwanie obiektów TocTree ze stron. Jest to przydatne, jeśli
dokumentacja korzysta z automatycznego generowania dokumentacji API,
co tworzy wiele stron zaślepkowych.

To rozszerzenie może być użyte do usunięcia odnośników na pasku
bocznym tylko do podanych stron, co istotnie przyspiesza budowanie.

%package apidocs
Summary:	API documentation for Python sphinx_remove_toctrees module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinx_remove_toctrees
Group:		Documentation

%description apidocs
API documentation for Python sphinx_remove_toctrees module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinx_remove_toctrees.

%prep
%setup -q -n sphinx_remove_toctrees-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sphinx_remove_toctrees
%{py3_sitescriptdir}/sphinx_remove_toctrees-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,second,*.html,*.js}
%endif
