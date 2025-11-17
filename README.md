A projektmappában megtalálható minden, amivel futtathatóvá lehet tenni az elkészített feladatomat.

node-red-data-helper mappa
2 dolgot tartalmaz, melyekre a konténerek elindítása után szükség van.
- package.json: Mivel a projekt tartalmaz további telepített extension-öket, ezeknek listája ebben a fájlban található meg. Ehhez a node-redben a 3 csík-ra kell menni - ott Manage Palette, ott pedig az Install fül alatt rákeresni a szükséges package-ekre és telepíteni.
- flows.json: Ezt kell importálni a node-red-be. Ez a fájl tartalmazza az elkészített Modbus-MQTT konverter logikáját.