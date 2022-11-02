CREATE TABLE `PartInformation` (
  `Index` INT,
  `WorkOrder` INT,
  `PartNumber` VARCHAR,
  `PartDescription` VARCHAR,
  `ToolLocation` VARCHAR,
  `Comment1` VARCHAR,
  `Comment2` VARCHAR,
  `Comment3` VARCHAR,
  `PartTCs` VARCHAR,
  `PartProbes` VARCHAR,
  `OtherSensors` VARCHAR,
  `EntryName` PK
);

CREATE TABLE `RunDetails` (
  `FileName` VARCHAR,
  `FilePath` VARCHAR,
  `LoadNumber` INT,
  `Equipment` VARCHAR,
  `RunRecipe` VARCHAR,
  `RunStart` VARCHAR,
  `RunEnd` VARCHAR,
  `RunDuration` VARCHAR,
  `OperatorName` VARCHAR,
  `ExportControl` VARCHAR,
  `EntryName` PK
);
