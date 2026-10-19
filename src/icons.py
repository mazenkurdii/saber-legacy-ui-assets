# Saber Legacy UI icon set. Each icon is drawn on a 128x128 canvas, white on
# transparent, inside a 16px safe margin. Rendered to one atlas sheet by build.py.
S = 'fill="none" stroke="#fff" stroke-width="9" stroke-linejoin="miter" stroke-linecap="square"'
T = 'fill="none" stroke="#fff" stroke-width="6" stroke-linejoin="miter" stroke-linecap="square"'
F = 'fill="#fff"'

ICONS = {
 # --- abilities -----------------------------------------------------------
 "Dash": f'''<path {S} d="M54 34 L84 64 L54 94"/><path {S} d="M80 34 L110 64 L80 94"/>
  <path {T} d="M18 50 H40 M10 64 H40 M18 78 H40"/>''',
 "Throw": f'''<path {S} d="M100 44 A40 40 0 1 0 104 78"/><path {F} d="M88 26 L116 40 L94 60 Z"/>
  <path stroke="#fff" stroke-width="7" stroke-linecap="round" d="M46 82 L82 46"/><rect {F} x="36" y="80" width="14" height="14" transform="rotate(45 43 87)"/>''',
 "Heavy": f'''<path {T} d="M30 18 A92 92 0 0 1 110 98"/><path stroke="#fff" stroke-width="8" stroke-linecap="round" d="M26 40 L78 92"/><path {F} d="M76 82 L88 94 L102 108 L94 116 L80 102 L68 90 Z"/>''',
 "Parry": f'''<path stroke="#fff" stroke-width="8" stroke-linecap="round" d="M24 24 L86 86 M104 24 L42 86"/>
  <path {F} d="M80 92 L92 80 L100 88 L88 100 Z M28 88 L40 100 L48 92 L36 80 Z"/>
  <circle {F} cx="64" cy="46" r="7"/>''',
 "ForcePush": f'''<circle {F} cx="28" cy="64" r="11"/><path {T} d="M50 40 A30 30 0 0 1 50 88"/>
  <path {T} d="M70 28 A44 44 0 0 1 70 100"/><path {T} d="M92 18 A58 58 0 0 1 92 110"/>''',
 "Ignite": f'''<rect {F} x="56" y="78" width="16" height="34"/><rect {F} x="52" y="72" width="24" height="8"/>
  <path stroke="#fff" stroke-width="8" stroke-linecap="round" d="M64 62 V14"/>''',
 # --- tabs ----------------------------------------------------------------
 "Inventory": f'''<path {S} d="M22 46 H106 V106 H22 Z"/><path {S} d="M44 46 V30 H84 V46"/><path {T} d="M22 70 H106 M56 70 V82 H72 V70"/>''',
 "Quests": f'''<path {S} d="M64 14 L108 40 V88 L64 114 L20 88 V40 Z"/><path {F} d="M58 36 H70 L68 74 H60 Z"/><rect {F} x="58" y="82" width="12" height="12"/>''',
 "Loadout": f'''<path stroke="#fff" stroke-width="8" stroke-linecap="round" d="M62 66 L110 18"/><path {F} d="M22 98 L56 64 L70 78 L36 112 Z"/><path fill="#000" d="M34 94 L44 84 L48 88 L38 98 Z M44 104 L54 94 L58 98 L48 108 Z"/><path {F} d="M52 60 L66 74 L72 68 L58 54 Z"/>''',
 "Vehicles": f'''<path {S} d="M12 70 L40 56 H96 L116 66 L96 76 H40 Z"/><path {T} d="M50 56 L62 40 H80"/><path {T} d="M30 92 H70 M84 92 H104"/>''',
 "Party": f'''<circle {S} cx="64" cy="42" r="14"/><path {S} d="M38 100 C38 76 90 76 90 100"/>
  <circle {T} cx="28" cy="52" r="10"/><path {T} d="M10 96 C10 80 30 74 40 80"/><circle {T} cx="100" cy="52" r="10"/><path {T} d="M118 96 C118 80 98 74 88 80"/>''',
 "Crafting": f'''<path {S} d="M38 90 L76 52"/><path {S} d="M70 34 A22 22 0 0 0 94 70 L86 58 L94 44 L80 50 Z"/><rect {F} x="18" y="86" width="26" height="26" transform="rotate(45 31 99)"/>''',
 "Shop": f'''<path {S} d="M24 44 H104 L96 110 H32 Z"/><path {T} d="M46 44 V32 A18 18 0 0 1 82 32 V44"/><path {F} d="M64 62 L76 76 L64 90 L52 76 Z"/>''',
 "Settings": f'''<path {S} d="M58 14 H70 L74 30 L86 36 L100 26 L108 34 L98 48 L104 60 L118 64 V70 L104 74 L98 86 L108 100 L100 108 L86 98 L74 104 L70 118 H58 L54 104 L42 98 L28 108 L20 100 L30 86 L24 74 L10 70 V64 L24 60 L30 48 L20 34 L28 26 L42 36 L54 30 Z"/><circle {S} cx="64" cy="67" r="15"/>''',
 # --- general -------------------------------------------------------------
 "Lock": f'''<path {S} d="M40 56 V40 A24 24 0 0 1 88 40 V56"/><rect {F} x="28" y="56" width="72" height="56"/><rect fill="#000" x="58" y="74" width="12" height="20"/>''',
 "Credits": f'''<path {S} d="M64 14 L108 39 V89 L64 114 L20 89 V39 Z"/><path {T} d="M64 38 V90 M50 52 H78 M50 76 H78"/>''',
 "Valuable": f'''<path {S} d="M34 26 H94 L114 50 L64 108 L14 50 Z"/><path {T} d="M14 50 H114 M46 26 L40 50 L64 108 L88 50 L82 26"/>''',
 "QuestItem": f'''<path {S} d="M64 14 L108 38 V90 L64 114 L20 90 V38 Z"/><path {T} d="M20 38 L64 62 L108 38 M64 62 V114"/><circle {F} cx="64" cy="40" r="6"/>''',
 "Speeder": f'''<path {S} d="M10 72 L30 58 H90 L118 66 L90 74 H30 Z"/><path {T} d="M58 58 L66 40 M14 90 H58 M70 90 H114"/>''',
 "Ship": f'''<path {S} d="M64 12 L82 70 L116 92 L116 104 L76 92 L64 110 L52 92 L12 104 L12 92 L46 70 Z"/><circle {F} cx="64" cy="58" r="7"/>''',
 "Shield": f'''<path {S} d="M64 12 L108 28 V60 C108 88 88 106 64 116 C40 106 20 88 20 60 V28 Z"/>''',
 "Player": f'''<circle {S} cx="64" cy="42" r="20"/><path {S} d="M24 112 C24 78 104 78 104 112"/>''',
 "Leader": f'''<path {F} d="M64 14 L78 48 L114 50 L86 72 L96 108 L64 88 L32 108 L42 72 L14 50 L50 48 Z"/>''',
 "Check": f'''<path stroke="#fff" stroke-width="12" fill="none" stroke-linecap="square" d="M22 66 L52 94 L106 34"/>''',
 "Duel": f'''<path stroke="#fff" stroke-width="8" stroke-linecap="round" d="M34 14 V72 M94 14 V72"/><rect {F} x="27" y="76" width="14" height="36"/><rect {F} x="87" y="76" width="14" height="36"/><path {T} d="M56 54 L72 54 M64 46 V62"/>''',
 "Safe": f'''<path {S} d="M64 12 L108 28 V60 C108 88 88 106 64 116 C40 106 20 88 20 60 V28 Z"/><path stroke="#fff" stroke-width="9" fill="none" d="M44 62 L58 76 L86 46"/>''',
 "Combat": f'''<path stroke="#fff" stroke-width="8" stroke-linecap="round" d="M22 22 L82 82 M106 22 L46 82"/><path {F} d="M76 88 L88 76 L106 94 L94 106 Z M52 88 L40 76 L22 94 L34 106 Z"/>''',
 "Close": f'''<path stroke="#fff" stroke-width="10" fill="none" d="M30 30 L98 98 M98 30 L30 98"/>''',
 "Back": f'''<path {S} d="M74 26 L36 64 L74 102"/>''',
 "Forward": f'''<path {S} d="M54 26 L92 64 L54 102"/>''',
 "Map": f'''<path {S} d="M16 30 L46 18 L82 30 L112 18 V98 L82 110 L46 98 L16 110 Z"/><path {T} d="M46 18 V98 M82 30 V110"/>''',
 "Friends": f'''<circle {S} cx="46" cy="44" r="16"/><path {S} d="M14 108 C14 78 78 78 78 108"/><path {T} d="M88 46 H116 M102 32 V60"/>''',
 "Invite": f'''<path {S} d="M16 34 H112 V100 H16 Z"/><path {T} d="M16 34 L64 72 L112 34"/>''',
 "Audio": f'''<path {F} d="M16 48 H38 L66 22 V106 L38 80 H16 Z"/><path {T} d="M82 44 A28 28 0 0 1 82 84 M96 30 A46 46 0 0 1 96 98"/>''',
 "Controls": f'''<rect {S} x="14" y="36" width="100" height="58" rx="2"/><path {T} d="M30 54 H40 M50 54 H60 M70 54 H80 M90 54 H100 M38 76 H90"/>''',
 "Interface": f'''<rect {S} x="14" y="24" width="100" height="80"/><path {T} d="M14 46 H114 M40 46 V104"/>''',
}
