Name:       mobile-broadband-provider-info
Summary:    Mobile Broadband Dataprovider Database
Version:    20251101
Release:    1
License:    Public Domain
BuildArch:  noarch
URL:        https://github.com/sailfishos/mobile-broadband-provider-info/
Source0:    %{name}-%{version}.tar.xz
BuildRequires: libxml2
BuildRequires: libxslt
BuildRequires: meson

# regenerate patch snippet:
# $  i=1; for j in 0*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
Patch0001: 0001-Added-MMS-settings.patch
Patch0002: 0002-Added-APN-settings-for-lands-Mobiltelefon.patch
Patch0003: 0003-Fixed-settings-for-Telenor-Norway.patch
Patch0004: 0004-Cleaned-up-MMS-settings-for-Orange-France.patch
Patch0005: 0005-Updated-MMS-settings-for-MTel-Bulgaria.patch
Patch0006: 0006-MMS-settings-for-3-DK.patch
Patch0007: 0007-MMS-settings-for-EMT-Estonia.patch
Patch0008: 0008-MMS-settings-for-Tele2-Sweden.patch
Patch0009: 0009-Added-MMS-settings-for-Vodafone-UK.patch
Patch0010: 0010-Replaced-mms.free.fr-with-its-IP-address.patch
Patch0011: 0011-gb-Distiguish-MNOs-primary-providers-from-MVNOs.patch
Patch0012: 0012-Updated-settings-for-CSL-Hong-Kong.patch
Patch0013: 0013-Updated-settings-for-3HK-Hong-Kong.patch
Patch0014: 0014-Updated-settings-for-PCCW-HK.patch
Patch0015: 0015-Plus-Poland-AP-settings.patch
Patch0016: 0016-Add-O2-UK-MMS-settings.patch
Patch0017: 0017-Add-O2-Germany-MMS-settings.patch
Patch0018: 0018-Airtel-India-MMS-APN-settings-added.patch
Patch0019: 0019-Added-the-name-for-Telenor-DK-internet-AP.patch
Patch0020: 0020-O2-Ireland-MMS-settings.patch
Patch0021: 0021-Virgin-Mobile-France-settings.patch
Patch0022: 0022-Orange-Austria-is-no-more.patch
Patch0023: 0023-Update-Tele2-Sweden-internet-and-MMS-settings.patch
Patch0024: 0024-Settings-for-Cricket-Wireless-USA.patch
Patch0025: 0025-Marked-Vodafone-DE-configuration-as-primary.patch
Patch0026: 0026-Moved-working-Telstra-AU-settings-to-the-top-of-the-.patch
Patch0027: 0027-LTE-compatible-configuration-for-Telekom-DE.patch
Patch0028: 0028-Telecom-Italia-settings.-Fixes-MER-896.patch
Patch0029: 0029-Updated-settings-for-3-UK.-MER-902.patch
Patch0030: 0030-Added-MCC-310-MNC-410-for-Cricket-Wireless.-MER-902.patch
Patch0031: 0031-Updated-settings-for-MegaFon-Russia.-MER-902.patch
Patch0032: 0032-Updated-settings-for-Telekom-HU.-MER-902.patch
Patch0033: 0033-Updated-settings-for-Etisalat-Du-Vodafone-NZ.-Added-.patch
Patch0034: 0034-in-Add-some-missing-Airtel-MCC-and-MNC-codes.patch
Patch0035: 0035-Added-missing-MNC-for-China-Mobile.-Contributes-to-M.patch
Patch0036: 0036-Added-MMS-settings-for-MTNL-India.-Contributes-to-JB.patch
Patch0037: 0037-Deleted-Polish-mobile-operators-which-don-t-exist-an.patch
Patch0038: 0038-Added-setup-for-SKTelecom-South-Korea-.-MER-902.patch
Patch0039: 0039-remove-non-existent-Polish-operators-mbank-freem-sam.patch
Patch0040: 0040-Added-setup-for-MOI-Finland-.-MER-902.patch
Patch0041: 0041-Cleaned-up-Free-France-settings.-MER-902.patch
Patch0042: 0042-Added-MMS-settings-for-3-Italy-.-MER-902.patch
Patch0043: 0043-Added-RebBullMobile-MVNO.-MER-902.patch
Patch0044: 0044-APN-settings-for-Yota-Russia-.-Fixes-JB-38857.patch
Patch0045: 0045-Added-Mobile-Vikings-MVNO.patch
Patch0046: 0046-Added-a2mobile-MVNO-and-remove-Nordisk-Polska-POLAND.patch
Patch0047: 0047-Housekeeping.patch
Patch0048: 0048-Changed-Beeline-AP-names-to-the-official-ones.-JB-37.patch
Patch0049: 0049-Use-PAP-authentication-for-Beeline-MMS-Russia-.-JB-3.patch
Patch0050: 0050-Added-apn-protocol-tag.-JB-39520.patch
Patch0051: 0051-Noverca-acquired-by-TIM-S.p.A-and-now-is-a-Full-MVNO.patch
Patch0052: 0052-Specify-auth-protocol-for-Telenor-Sweden-MMS-access-.patch
Patch0053: 0053-Updated-settings-for-Vietnam.-Fixes-JB-48358.patch
Patch0054: 0054-Update-for-Polish-networks.-MER-902.patch
Patch0055: 0055-Update-of-Kazakh-and-Kyrgyz-operators.-MER-902.patch
Patch0056: 0056-APN-settings-for-Letai-Russia-.-Fixes-JB-51615.patch
Patch0057: 0057-Add-APN-settings-for-ROSTELECOM-Russia-.-Fixes-JB-53.patch
Patch0058: 0058-Update-Polish-network-Play.patch
Patch0059: 0059-Remove-Polish-mobile-network-Cyfrowy-Polsat.patch
Patch0060: 0060-Fello-added-in-Swedish-providers-section.patch
Patch0061: 0061-Otvarta-and-UPS-Polska-added-to-Polish-providers-sec.patch
Patch0062: 0062-Update-for-french-auchan-telecom.patch
Patch0063: 0063-update-for-georgian-providers.patch
Patch0064: 0064-azeri-providers-update.patch
Patch0065: 0065-Iceland-providers-update.patch
Patch0066: 0066-Marocco-providers-update.patch
Patch0067: 0067-Montenegro-providers-update.patch
Patch0068: 0068-Iran-and-Iraq-providers-update.patch
Patch0069: 0069-Update-Afgan-provider-and-remove-one-from-Australia.patch
Patch0070: 0070-United-Arab-Emirates-providers-update.patch
Patch0071: 0071-Fix-Orange-Belgium-network-APN.patch
Patch0072: 0072-Adding-Voicemail-number-on-the-Belgium-Orange-Networ.patch
Patch0073: 0073-Add-back-auhentication-method-any.patch

%description
This package contains mobile broadband settings for different service providers
in different countries. The Package contains only informational files so it's
safe for distributions to grab updates even during feature freeze and
maintenance stages.

When you want to configure a mobile broadband connections there usually is some
service provider specific information you have to know before the connection
can be established. Problem with this information is that it's highly technical
for an ordinary consumer and it's available only from service providers web
page or from Microsoft Windows installation media that becomes with tie-in
subscription devices.

The interesting side of this information is that it's the same for every user
of a given service provider. This means that service provider specific 
information can be stored in a database. When this database is available the
information can be fetched there and the ordinary user does not need to bother
about it. 

Service provider specific information is stored in a XML file. XML is not the
most optimized format for a database, but it's easy to read, understand and
edit.

The database is released under Creative Commons Public Domain (CC-PD).

%package devel
Summary:    Development files for mobile-broadband-provider-info package
Requires:   %{name} = %{version}-%{release}

%description devel
Contains development files for mobile-broadband-provider-info, e.g., .pc file.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson
%meson_build

%install
%meson_install

%check
xmllint --noout --dtdvalid serviceproviders.2.dtd serviceproviders.xml

%files
%license COPYING
%{_datadir}/mobile-broadband-provider-info

%files devel
%doc README
%{_datadir}/pkgconfig/mobile-broadband-provider-info.pc
