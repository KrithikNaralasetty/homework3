#!/bin/bash
echo "Creating a virtual machine"
VBoxManage createvm --name database --ostype "Ubuntu-64" --register --basefolder "C:\Users\krith\Desktop\Important\MS\CC\Assignments\HW3\VM"

VBoxManage modifyvm database --ioapic on --vram 128 --memory 2048 --nic1 nat --cpus 2

VBoxManage createhd --filename "C:\Users\krith\Desktop\Important\MS\CC\Assignments\HW3\VM\database\database_DISK.VDI" --size 30000 --format VDI

VBoxManage storagectl database --name "SATA Controller" --add sata --controller IntelAhci

VBoxManage storageattach database --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "C:\Users\krith\Desktop\Important\MS\CC\Assignments\HW3\VM\database\database_DISK.VDI"

VBoxManage storagectl database --name "IDE Controller" --add ide --controller PIIX4

VBoxManage storageattach database --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium "/home/Krithik/Desktop/VM/debian.iso"

VBoxManage modifyvm database --boot1 dvd --boot2 disk --boot3 none --boot4 none

VBoxManage startvm database