https://apple.stackexchange.com/questions/13598/updating-modifier-key-mappings-through-defaults-command-tool


# The apple keyboard id (1452-567-0) should probably be modified in case you use other different model 
```
COMPUTER_UUID=`ioreg -rd1 -c IOPlatformExpertDevice | grep -E '(UUID)' | awk '{print $3}' | tr -d \"`
defaults write ~/Library/Preferences/ByHost/.GlobalPreferences.$COMPUTER_UUID com.apple.keyboard.modifiermapping.1452-567-0 '( { HIDKeyboardModifierMappingDst = 2;   HIDKeyboardModifierMappingSrc = 0; } )'
```

Turns off capslock
```
defaults -currentHost write -g com.apple.keyboard.modifiermapping.1118-219-0 -array-add '<dict><key>HIDKeyboardModifierMappingDst</key><integer>-1</integer><key>HIDKeyboardModifierMappingSrc</key><integer>0</integer></dict>'
```



This is what it looks like when Caps Lock and Ctl are switched (with
something extra thrown in):
```
Found 2 keys in domain 'Apple Global Domain': {
    "com.apple.keyboard.modifiermapping.1452-591-0" =     (
                {
            HIDKeyboardModifierMappingDst = 30064771296;
            HIDKeyboardModifierMappingSrc = 30064771129;
        },
                {
            HIDKeyboardModifierMappingDst = 30064771129;
            HIDKeyboardModifierMappingSrc = 30064771296;
        },
                {
            HIDKeyboardModifierMappingDst = 30064771129;
            HIDKeyboardModifierMappingSrc = 30064771300;
        }
    );
    "com.apple.keyboard.modifiermapping.1452-628-0" =     (
                {
            HIDKeyboardModifierMappingDst = 30064771296;
            HIDKeyboardModifierMappingSrc = 30064771129;
        },
                {
            HIDKeyboardModifierMappingDst = 30064771129;
            HIDKeyboardModifierMappingSrc = 30064771296;
        },
                {
            HIDKeyboardModifierMappingDst = 30064771129;
            HIDKeyboardModifierMappingSrc = 30064771300;
        }
    );
}
```
