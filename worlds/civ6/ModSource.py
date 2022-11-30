# Note: some of this SQL code is vulnerable to injections. The code assumes that the strings
# in the scope do not contain dollar signs or quotes.

mod_src = """
#FILE Archipelago.modinfo
<?xml version="1.0" encoding="utf-8"?>
<Mod id="1e9900a0-e697-4caa-9967-0253bd51176a" version="1">
  <Properties>
    <Name>Archipelago</Name>
    <Description>Randomizes techs and civics with items from other games</Description>
    <Created>1090454400</Created>
    <Teaser>Randomizes techs and civics with items from other games</Teaser>
    <Authors>Seldom</Authors>
    <CompatibleVersions>2.0</CompatibleVersions>
  </Properties>
  <ActionCriteria>
    <Criteria id="SetItems">
      <ConfigurationValueMatches>
        <ConfigurationId>WW_SET_ITEMS</ConfigurationId>
        <Group>Game</Group>
        <Value>1</Value>
      </ConfigurationValueMatches>
    </Criteria>
  </ActionCriteria>
  <InGameActions>
    <UpdateDatabase id="WW_Set_Items">
      <Properties>
        <LoadOrder>44700</LoadOrder>
      </Properties>
      <Criteria>SetItems</Criteria>
      <File>SetItems.sql</File>
    </UpdateDatabase>
  </InGameActions>
  <Files>
    <File>SetItems.sql</File>
  </Files>
</Mod>
#FILE SetItems.sql
CREATE TABLE TechnologiesTemp
  LIKE Technologies;

CREATE TABLE CivicsTemp
  LIKE Civics;

CREATE TABLE TechnologyPrereqsTemp
  LIKE TechnologyPrereqs;

INSERT INTO TechnologyPrereqsTemp
  SELECT *
    FROM TechnologyPrereqs;

CREATE TABLE CivicPrereqsTemp
  LIKE CivicPrereqs;

INSERT INTO CivicPrereqsTemp
  SELECT *
    FROM CivicPrereqs;

#FOR $CHECKS$
INSERT INTO
#IF $TECH$ 
  TechnologiesTemp (
    TechnologyType,
    Critical,
#ELSE
  CivicsTemp (
    CivicType,
#END
    Name,
    EraType,
    UITreeRow,
    Cost,
    EmbarkUnitType,
    EmbarkAll,
    Description,
    BarbarianFree,
    AdvisorType
  )
  SELECT (
    "$TYPE$",
#IF $TECH$
#IF $VANILLA$
    Src.Critical,
#ELSE
    0,
#END
#ELSE
#END
    "$NAME$",
    Pos.EraType,
    Pos.UITreeRow,
#IF $VANILLA$
    Src.Cost,
    Src.EmbarkUnitType,
    Src.EmbarkAll,
    Src.Description,
    Src.BarbarianFree,
    Src.AdvisorType,
#ELSE
    Pos.Cost,
    NULL,
    0,
    "$DESC$",
    0,
    "ADVISOR_GENERIC",
#END
  )
    FROM
#IF $TECH$
      Technologies Pos
      WHERE Pos.TechnologyType
#ELSE
      Civics Pos
      WHERE Pos.CivicType
#END
        = "$POS_TYPE$"
#IF $VANILLA$
      INNER JOIN
#IF $TECH$
        Technologies Src
        ON Src.TechnologyType
#ELSE
        Civics Src
        ON Src.CivicType
#END
          = "$SRC_TYPE$";
#ELSE
;
#END

UPDATE
#IF $TECH$
  TechnologyPrereqsTemp
  SET Technology = "$TYPE$"
  WHERE Technology
#ELSE
  CivicPrereqsTemp
  SET Civic = "$TYPE$"
  WHERE Civic
#END
    = "$POS_TYPE$";

UPDATE
#IF $TECH$
  TechnologyPrereqsTemp
  SET PrereqTech = "$TYPE$"
  WHERE PrereqTech
#ELSE
  CivicPrereqsTemp
  SET PrereqCivic = "$TYPE$"
  WHERE PrereqCivic
#END
    = "$POS_TYPE$";
#END

#FOR $EMIGRANTS$
INSERT INTO
#IF $TECH$
  TechnologiesTemp
  SELECT * FROM Technologies
  WHERE TechnologyType
#ELSE
  CivicsTemp
  SELECT * FROM Civics
  WHERE CivicType
#END
    = "$TYPE$";

UPDATE
#IF $TECH$
  TechnologiesTemp
#ELSE
  CivicsTemp
#END
  SET Cost = -1, UITreeRow = -4
  WHERE
#IF $TECH$
    TechnologyType
#ELSE
    CivicType
#END
    = "$TYPE$";

DROP TABLE Technologies;

ALTER TABLE TechnologiesTemp
  RENAME TO Technologies;

DROP TABLE Civics;

ALTER TABLE CivicsTemp
  RENAME TO Civics;

DROP TABLE TechnologyPrereqs;

ALTER TABLE TechnologyPrereqsTemp
  RENAME TO TechnologyPrereqs;

DROP TABLE CivicPrereqs;

ALTER TABLE CivicPrereqsTemp
  RENAME TO CivicPrereqs;
"""
