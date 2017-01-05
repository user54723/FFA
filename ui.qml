import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1
import QtQuick.Dialogs 1.1

ApplicationWindow {
    visible: true
    title: "Audiométrie en champs libre"
    width: 800
    height: 600

    RowLayout {
        id : 
        ColumnLayout {
           
           id: word
                   
    }
    GridLayout {
        id: tabView

        anchors.fill: parent
        anchors.margins: UI.margin
        tabPosition: UI.tabPosition

        Layout.minimumWidth: 360
        Layout.minimumHeight: 360
        Layout.preferredWidth: 480
        Layout.preferredHeight: 640

        Tab {
            title: "Buttons"
            ButtonPage {
                enabled: enabler.checked
            }
        }
        Tab {
            title: "Progress"
            ProgressPage {
                enabled: enabler.checked
            }
        }
        Tab {
            title: "Input"
            InputPage {
                enabled: enabler.checked
            }
        }
    }
}