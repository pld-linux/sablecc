Name:		sablecc
Version:	2.17.2
Release:	0.1
Summary:	sablecc
License:	LGPL
Group:		Development/Languages/Java
URL:		http://sablecc.sf.net
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}-src.tar.gz
# Source0-md5:	62b84770389f82d997ddf832fa535191
BuildRequires:	jakarta-ant >= 1.5
BuildRequires:	xerces-j
BuildConflicts:	sablecc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
sablecc

%prep
%setup -q -n %{name}-%{version}

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
