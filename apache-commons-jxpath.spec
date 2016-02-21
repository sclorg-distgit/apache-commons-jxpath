%global pkg_name apache-commons-jxpath
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global base_name       jxpath
%global short_name      commons-%{base_name}

Name:             %{?scl_prefix}%{pkg_name}
Version:          1.3
Release:          20.13%{?dist}
Summary:          Simple XPath interpreter

License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:           %{short_name}-mockrunner.patch
BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}javapackages-tools
BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix}apache-commons-parent >= 26-7
BuildRequires:    %{?scl_prefix}maven-antrun-plugin
BuildRequires:    %{?scl_prefix}maven-assembly-plugin
BuildRequires:    %{?scl_prefix}maven-compiler-plugin
BuildRequires:    %{?scl_prefix}maven-install-plugin
BuildRequires:    %{?scl_prefix}maven-jar-plugin
BuildRequires:    %{?scl_prefix}maven-javadoc-plugin
BuildRequires:    %{?scl_prefix}maven-plugin-bundle
BuildRequires:    %{?scl_prefix}maven-resources-plugin
BuildRequires:    %{?scl_prefix}maven-surefire-plugin
BuildRequires:    %{?scl_prefix_java_common}mvn(javax.servlet:javax.servlet-api)
BuildRequires:    %{?scl_prefix_java_common}mvn(javax.servlet:jsp-api)


%description
Defines a simple interpreter of an expression language called XPath.
JXPath applies XPath expressions to graphs of objects of all kinds:
JavaBeans, Maps, Servlet contexts, DOM etc, including mixtures thereof.

%package javadoc
Summary:          API documentation for %{pkg_name}


%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%patch0 -p1
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# we are skipping tests because we don't have com.mockrunner in repos yet
%mvn_file  : %{short_name} %{pkg_name}
%mvn_alias : org.apache.commons:%{short_name}
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.3-20.13
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.3-20.12
- maven33 rebuild

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.11
- Fix BR on EE APIs

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.3-20.11
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 1.3-20.10
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.3-20.9
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.8
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.7
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.6
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.5
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.4
- Rebuild to fix incorrect auto-requires

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3-20
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-19
- Add BuildRequires on apache-commons-parent >= 26-7

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-18
- Remove workaround for rpm bug #646523

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-17
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-16
- Remove unneeded BR: maven-idea-plugin

* Tue Feb 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-15
- Migrate from Tomcat 6 to Tomcat 7
- Resolves: rhbz#913879

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Michal Srb <msrb@redhat.com> - 1.3-12
- Build with xmvn

* Thu Nov 22 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-11
- Install NOTICE file
- Resolves: rhbz#879556

* Fri Nov  9 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-10
- Don't build-require maven2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  2 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> 1.3-8
- Fix build and update to latest guidelines

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 21 2010 Chris Spike <chris.spike@arcor.de> 1.3-5
- tomcat5 -> tomcat6 BRs/Rs

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-4
- Add license to javadoc subpackage

* Thu May 27 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-3
- Add tomcat5 to BR

* Tue May 25 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-2
- Fix ownership of some directories

* Tue May 25 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-1
- Rename package (jakarta-commons-jxpath->apache-commons-jxpath)
- Cleanup spec file
- Build using maven, drop old pom file from sources
- Update to upstream version

* Thu Aug 20 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-9
- Fix random spaces.

* Wed Aug 19 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-8
- BuildRequires java-devel >= 1.6.0.

* Wed Aug 19 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-7
- Initial package for Fedora.

* Sun May 17 2009 Fernando Nasser <fnasser@redhat.com> - 0:1.2-6
- Fix License
- Provide intructions for obtaining source and refresh source tar ball

* Wed Mar 18 2009 Yong Yang <yyang@redhat.com> - 0:1.2-5
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Thu Feb 05 2009 Yong Yang <yyang@redhat.com> - 0:1.2-4
- Fix release tag

* Thu Jan 08 2009 Yong Yang <yyang@redhat.com> - 0:1.2-3jpp.1
- Import from dbhole's maven 2.0.8 packages, initial building

* Wed Apr 09 2008 Deepak Bhole <dbhole@redhat.com> - 0:1.2-2jpp.1
- Import from JPackage
- Added pom file

* Wed Jun 07 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.2-2jpp
- First JPP 1.7 build

* Sat Sep 18 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.2-1jpp
- Upgrade to 1.2
- Use jdom-1.0-0.rc1.1jpp
- Relax some versioned dependencies

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.1-3jpp
- Rebuild with ant-1.6.2

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:1.1-2jpp
- Upgrade to Ant 1.6.X

* Mon Jan 19 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.1-1jpp
- First JPackage release
