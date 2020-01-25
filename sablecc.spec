Summary:	SableCC - the Sable Research Group's Compiler Compiler
Summary(pl.UTF-8):	SableCC - kompilator kompilatorów z Sable Research Group
Name:		sablecc
Version:	3.2
Release:	0.2
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://downloads.sourceforge.net/sablecc/%{name}-%{version}.zip
# Source0-md5:	0c38a98fddc374e5d4b67bf4c2ff4c19
URL:		http://sablecc.sourceforge.net/
BuildRequires:	ant >= 1.5
BuildRequires:	java-xerces
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SableCC is an object-oriented framework that generates compilers (and
interpreters) in the Java programming language. This framework is
based on two fundamental design decisions. Firstly, the framework uses
object-oriented techniques to automatically build a strictly typed
abstract syntax tree that matches the grammar of the compiled language
and simplifies debugging. Secondly, the framework generates
tree-walker classes using an extended version of the visitor design
pattern which enables the implementation of actions on the nodes of
the abstract syntax tree using inheritance. These two design decisions
lead to a tool that supports a shorter development cycle for
constructing compilers.

%description -l pl.UTF-8
SableCC to obiektowo zorientowany szkielet generujący kompilatory
(oraz interpretery) w języku programowania Java. Ten szkielet bazuje
na dwóch fundamentalnych decyzjach projektowych. Po pierwsze, szkielet
używa technik zorientowanych obiektowo do automatycznego zbudowania
abstrakcyjnego drzewa składni ze ścisłymi typami, zgodnego z gramatyką
kompilowanego języka oraz upraszczającego odpluskwianie. Po drugie,
szkielet ten generuje klasy chodzące po drzewach przy użyciu
rozszerzonej wersji wzorca, co pozwala na implementowanie akcji dla
węzłów abstrakcyjnego drzewa składni przy użyciu dziedziczenia. Te
dwie decyzje projektowe dają narzędzie wspierające krótszy cykl
produkcji przy konstruowaniu kompilatorów.

%prep
%setup -q

cat > bin/sablecc <<'EOF'
#!/bin/sh

exec java -jar %{_javadir}/%{name}.jar "$@"
EOF

%build
%ant jar
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_bindir}}

cp -p lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -p bin/sablecc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.html THANKS
%attr(755,root,root) %{_bindir}/sablecc
%{_javadir}/*.jar
