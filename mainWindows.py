# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WikiGenerator(object):
    def setupUi(self, WikiGenerator):
        WikiGenerator.setObjectName("WikiGenerator")
        WikiGenerator.resize(802, 738)
        self.centralwidget = QtWidgets.QWidget(WikiGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.rsi = QtWidgets.QLabel(self.centralwidget)
        self.rsi.setGeometry(QtCore.QRect(180, 310, 111, 25))
        self.rsi.setObjectName("rsi")
        self.jenkins_ = QtWidgets.QLineEdit(self.centralwidget)
        self.jenkins_.setGeometry(QtCore.QRect(340, 250, 311, 31))
        self.jenkins_.setObjectName("jenkins_")
        self.lastcommit = QtWidgets.QLabel(self.centralwidget)
        self.lastcommit.setGeometry(QtCore.QRect(180, 190, 111, 25))
        self.lastcommit.setObjectName("lastcommit")
        self.hmi = QtWidgets.QLabel(self.centralwidget)
        self.hmi.setGeometry(QtCore.QRect(180, 70, 131, 25))
        self.hmi.setObjectName("hmi")
        self.jenkins = QtWidgets.QLabel(self.centralwidget)
        self.jenkins.setGeometry(QtCore.QRect(180, 250, 111, 25))
        self.jenkins.setObjectName("jenkins")
        self.hmi_ = QtWidgets.QLineEdit(self.centralwidget)
        self.hmi_.setGeometry(QtCore.QRect(340, 70, 311, 31))
        self.hmi_.setText("")
        self.hmi_.setObjectName("hmi_")
        self.lastcommit_ = QtWidgets.QLineEdit(self.centralwidget)
        self.lastcommit_.setGeometry(QtCore.QRect(340, 190, 311, 31))
        self.lastcommit_.setObjectName("lastcommit_")
        self.branch_ = QtWidgets.QLineEdit(self.centralwidget)
        self.branch_.setGeometry(QtCore.QRect(340, 130, 311, 31))
        self.branch_.setObjectName("branch_")
        self.rsi_ = QtWidgets.QLineEdit(self.centralwidget)
        self.rsi_.setGeometry(QtCore.QRect(340, 310, 311, 31))
        self.rsi_.setObjectName("rsi_")
        self.branch = QtWidgets.QLabel(self.centralwidget)
        self.branch.setGeometry(QtCore.QRect(180, 130, 111, 25))
        self.branch.setObjectName("branch")
        self.summit_HMI = QtWidgets.QPushButton(self.centralwidget)
        self.summit_HMI.setGeometry(QtCore.QRect(180, 370, 471, 46))
        self.summit_HMI.setObjectName("summit_HMI")
        self.java_ = QtWidgets.QLineEdit(self.centralwidget)
        self.java_.setGeometry(QtCore.QRect(340, 460, 311, 31))
        self.java_.setText("")
        self.java_.setObjectName("java_")
        self.summit_JavaSDK = QtWidgets.QPushButton(self.centralwidget)
        self.summit_JavaSDK.setGeometry(QtCore.QRect(180, 640, 471, 46))
        self.summit_JavaSDK.setObjectName("summit_JavaSDK")
        self._jenkins_java = QtWidgets.QLineEdit(self.centralwidget)
        self._jenkins_java.setGeometry(QtCore.QRect(340, 580, 311, 31))
        self._jenkins_java.setObjectName("_jenkins_java")
        self.jenkins_java = QtWidgets.QLabel(self.centralwidget)
        self.jenkins_java.setGeometry(QtCore.QRect(180, 580, 111, 25))
        self.jenkins_java.setObjectName("jenkins_java")
        self.lastcommit_java_ = QtWidgets.QLineEdit(self.centralwidget)
        self.lastcommit_java_.setGeometry(QtCore.QRect(340, 520, 311, 31))
        self.lastcommit_java_.setObjectName("lastcommit_java_")
        self.java = QtWidgets.QLabel(self.centralwidget)
        self.java.setGeometry(QtCore.QRect(180, 460, 151, 25))
        self.java.setObjectName("java")
        self.lastcommit_java = QtWidgets.QLabel(self.centralwidget)
        self.lastcommit_java.setGeometry(QtCore.QRect(180, 520, 111, 25))
        self.lastcommit_java.setObjectName("lastcommit_java")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 20, 471, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        WikiGenerator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WikiGenerator)
        self.statusbar.setObjectName("statusbar")
        WikiGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(WikiGenerator)
        QtCore.QMetaObject.connectSlotsByName(WikiGenerator)

    def retranslateUi(self, WikiGenerator):
        _translate = QtCore.QCoreApplication.translate
        WikiGenerator.setWindowTitle(_translate("WikiGenerator", "WikiGenerator"))
        self.rsi.setText(_translate("WikiGenerator", "RSI VERSION"))
        self.lastcommit.setText(_translate("WikiGenerator", "Last commit"))
        self.hmi.setText(_translate("WikiGenerator", "HMI VERSION"))
        self.jenkins.setText(_translate("WikiGenerator", "Jenkins"))
        self.branch.setText(_translate("WikiGenerator", "Branch Name"))
        self.summit_HMI.setText(_translate("WikiGenerator", "Summit_HMI"))
        self.summit_JavaSDK.setText(_translate("WikiGenerator", "Summit_JavaSDK"))
        self.jenkins_java.setText(_translate("WikiGenerator", "Jenkins"))
        self.comboBox.setItemText(0, _translate("WikiGenerator", "Denali"))
        self.comboBox.setItemText(1, _translate("WikiGenerator", "Rainier"))
        self.java.setText(_translate("WikiGenerator", "Java VERSION"))
        self.lastcommit_java.setText(_translate("WikiGenerator", "Last commit"))

        self.summit_HMI.clicked.connect(self.hmi_wiki)
        self.summit_JavaSDK.clicked.connect(self.java_wiki)
        self.comboBox.activated.connect(self.project_select)
    def project_select(self):
        _translate = QtCore.QCoreApplication.translate
        if(self.comboBox.currentText() == 'Denali'):
            self.java.setText(_translate("WikiGenerator", "JavaSDK VERSION"))
        elif(self.comboBox.currentText() == 'Rainier'):
            self.java.setText(_translate("WikiGenerator", "AtlasSDK VERSION"))
    def hmi_wiki(self):
        hmiVersion = self.hmi_.text()
        branchName = self.branch_.text()
        lastCommit_hmi = self.lastcommit_.text()
        lastCommit_title_hmi = self.lastcommit_.text()[-40: -32]
        jenkins = self.jenkins_.text()
        rsi = self.rsi_.text()
        if(self.comboBox.currentText() == 'Denali'):
            hmi_content = '''
**HMI:**

- GIT: https://bitbucket.telenav.com/projects/AUT/repos/hmi-common/browse?at=refs%2Fheads%2Frelease%2F{_branchName}
- Last commit: [{_lastCommit_title}]({_lastCommit})
- Jenkins Flow: [{_jenkins}]({_jenkins})
- HMI APK(HU): [denali-android-x86_64-{_hmiVersion}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/Denali/release/{_branchName}/RC/{_hmiVersion}/Artifacts/denali-android-x86_64-{_hmiVersion}-signed.apk)
- HMI APK(X86_64 Tablet): [denali-android-x86_64-tablet-{_hmiVersion}8-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/Denali/release/{_branchName}/RC/{_hmiVersion}/Artifacts/denali-android-x86_64-tablet-{_hmiVersion}-signed.apk)
- Version: {_hmiVersion}
- HMI APK(Armv7a Tablet): [denali-android-armv7a-tablet-{_hmiVersion}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/Denali/release/{_branchName}/RC/{_hmiVersion}/Artifacts/denali-android-armv7a-tablet-{_hmiVersion}-signed.apk)
- Release note: http://tar2.telenav.com/repository/telenav/HMI-Common/Denali/release/{_branchName}/RC/{_hmiVersion}/ReleaseNote/release_note.html
- HMI APK(Production): [production-denali-x86_64-android-{_hmiVersion}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/Denali/release/{_branchName}/RC/{_hmiVersion}/Artifacts/production-denali-x86_64-android-{_hmiVersion}-signed.apk)
- GM Jenkins: 
- Home Screen: 
- prebuild:


**RSI:**

- RSI1: [rsi1-{_rsi}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/RSI/release/{_branchName}/RC/{_rsi}/Artifacts/rsi1-{_rsi}-signed.apk)
- RSI2: [rsi2-{_rsi}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/RSI/release/{_branchName}/RC/{_rsi}/Artifacts/rsi2-{_rsi}-signed.apk)   
            '''.format(_branchName=branchName, _lastCommit_title=lastCommit_title_hmi, _jenkins=jenkins,
                       _hmiVersion=hmiVersion,
                       _lastCommit=lastCommit_hmi, _rsi=rsi)
        elif(self.comboBox.currentText() == 'Rainier'):
            hmi_content = '''       
**HMI:**

- Jenkins Job:[{_jenkins}]({_jenkins})
- Last commit for build: [{_lastCommit_title}]({_lastCommit})
- Coverage report: [CoverageReport/](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/CoverageReport/)
- Security report: [SecurityAnalysisReport/](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/SecurityAnalysisReport/)
- Static code analysis report: [StaticCodeAnalysisReport/](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/StaticCodeAnalysisReport/)
- Unit test report: [UnitTestReport/](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/UnitTestReport/)
- Git branch: [release/{_branchName}](https://bitbucket.telenav.com/projects/AUT/repos/hmi-common/browse?at=refs%2Fheads%2Frelease%2F{_branchName})
- Version: [{_hmiVersion}](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/)
- Bench(x86_64)
- HMI APK: [rainier-dev-release-x86_64-{_hmiVersion}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/Artifacts/rainier-dev-release-x86_64-{_hmiVersion}-signed.apk)
- So libraries: [solibs-{_hmiVersion}.zip](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/Artifacts/solibs-{_hmiVersion}.zip)
- HMI PRD APK: [rainier-production-release-x86_64-{_hmiVersion}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/Artifacts/rainier-production-release-x86_64-{_hmiVersion}-signed.apk)

**Cluster:**

- Cluster: [cluster-x86_64-{_hmiVersion}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/Rainier/release/{_branchName}/RC/{_hmiVersion}/Artifacts/cluster-x86_64-{_hmiVersion}-signed.apk)

**RSI:**

- Security report: [SecurityAnalysisReport/](http://tar2.telenav.com/repository/telenav/HMI-Common/RSI/release/{_branchName}/RC/{_rsi}/SecurityAnalysisReport/)
- Static code analysis report: [StaticCodeAnalysisReport/](http://tar2.telenav.com/repository/telenav/HMI-Common/RSI/release/{_branchName}/RC/{_rsi}/StaticCodeAnalysisReport/)
- RSI1: [rsi1-x86_64-{_rsi}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/RSI/release/{_branchName}/RC/{_rsi}/Artifacts/rsi1-x86_64-{_rsi}-signed.apk)
- RSI2: [rsi2-x86_64-{_rsi}-signed.apk](http://tar2.telenav.com/repository/telenav/HMI-Common/RSI/release/{_branchName}/RC/{_rsi}/Artifacts/rsi2-x86_64-{_rsi}-signed.apk)
                       '''.format(_branchName=branchName, _lastCommit_title=lastCommit_title_hmi, _jenkins=jenkins,
                                  _hmiVersion=hmiVersion,
                                  _lastCommit=lastCommit_hmi, _rsi=rsi)

        with open('hmi.txt', 'w') as f:
            f.write(hmi_content)
        f.close()
        QtWidgets.QMessageBox.information(self.summit_HMI,"INFO", "Has been saved in hmi.txt")

    def java_wiki(self):
        branchName = self.branch_.text()
        javaVersion = self.java_.text()
        lastCommit_java = self.lastcommit_java_.text()
        lastCommit_title_java = self.lastcommit_java_.text()[-40: -32]
        jenkins_java = self._jenkins_java.text()
        if (self.comboBox.currentText() == 'Denali'):
            java_content = '''
        
**JavaSDK**

- GIT branch: https://bitbucket.telenav.com/projects/AUT/repos/java-sdk-common/browse?at=refs%2Fheads%2Frelease%2F{_branchName}
- Last commit: [{_lastCommit_title}]({_lastCommit})
- Jenkins Flow:  [{_jenkins}]({_jenkins})
- Release note: http://tar2.telenav.com/repository/telenav/Common-Lib/SDK/{_javaVersion}/
- Version: {_javaVersion}
- PL3 test tool: http://tar2.telenav.com/repository/telenav/Common-Lib/SDK/{_javaVersion}/arp-sdk-debug-test-android-{_javaVersion}.apk
            '''.format(_branchName=branchName, _lastCommit_title=lastCommit_title_java, _jenkins=jenkins_java,
                       _javaVersion=javaVersion, _lastCommit=lastCommit_java)
        elif(self.comboBox.currentText() == 'Rainier'):
            java_content = '''

**JavaSDK**


- Git: [release/{_branchName}](https://bitbucket.telenav.com/projects/AUT/repos/java-sdk-common/browse?at=refs%2Fheads%2Frelease%2F{_branchName})
- Last commit for build: [{_lastCommit_title}]({_lastCommit})
- Jenkins: [{_jenkins}]({_jenkins})
- Atlas SDK Version: [{_javaVersion}/](http://tar2.telenav.com/repository/telenav/Common-Lib/SDK/{_javaVersion}/)
- Pipleline test tool:  [arp-sdk-debug-test-android-{_javaVersion}.apk](http://tar2.telenav.com/repository/telenav/Common-Lib/SDK/{_javaVersion}/arp-sdk-debug-test-android-{_javaVersion}.apk)

            '''.format(_branchName=branchName, _lastCommit_title=lastCommit_title_java,
                       _jenkins=jenkins_java,
                       _javaVersion=javaVersion, _lastCommit=lastCommit_java)

        with open('java.txt', 'w') as m:
             m.write(java_content)
        m.close()
        QtWidgets.QMessageBox.information(self.summit_HMI, "INFO", "Has been saved in java.txt")

