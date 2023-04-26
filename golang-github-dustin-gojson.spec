# Generated by go2rpm 1.9.0
%bcond_with check
%global debug_package %{nil}

# https://github.com/dustin/gojson
%global goipath         github.com/dustin/gojson
%global commit          2e71ec9dd5adce3b168cd0dbde03b5cc04951c30

%gometa -f


%global common_description %{expand:
Fork of go's encoding/json with the scanner API made public.}

%global golicenses      LICENSE
Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Fork of go's encoding/json with the scanner API made public

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
