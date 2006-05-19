Summary:	SableCC - the Sable Research Group's Compiler Compiler
Summary(pl):	SableCC - kompilator kompilatorów z Sable Research Group
Name:		sablecc
Version:	2.17.2
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
# Source0-md5:	62b84770389f82d997ddf832fa535191
URL:		http://sablecc.sf.net/
BuildRequires:	ant >= 1.5
BuildRequires:	xerces-j
BuildConflicts:	sablecc
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

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

%description -l pl
SableCC to obiektowo zorientowany szkielet generuj±cy kompilatory
(oraz interpretery) w jêzyku programowania Java. Ten szkielet bazuje
na dwóch fundamentalnych decyzjach projektowych. Po pierwsze, szkielet
u¿ywa technik zorientowanych obiektowo do automatycznego zbudowania
abstrakcyjnego drzewa sk³adni ze ¶cis³ymi typami, zgodnego z gramatyk±
kompilowanego jêzyka oraz upraszczaj±cego odpluskwianie. Po drugie,
szkielet ten generuje klasy chodz±ce po drzewach przy u¿yciu
rozszerzonej wersji wzorca, co pozwala na implementowanie akcji dla
wêz³ów abstrakcyjnego drzewa sk³adni przy u¿yciu dziedziczenia. Te
dwie decyzje projektowe daj± narzêdzie wspieraj±ce krótszy cykl
produkcji przy konstruowaniu kompilatorów.

%prep
%setup -q

%build
ant jar

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
cp lib/%{name}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.html THANKS
%{_javalibdir}/*.jar
