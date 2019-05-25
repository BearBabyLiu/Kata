package main.scala.com.liuhuang

case class ParamExtract(inputParm: String, schemaStr: String) {
  val cmdLineArgInst = new CommandLineArgs(inputParm)
  val schemaParser = new SchemaParser(schemaStr)

  def getFlagValue(flag: String): Any = {
    schemaParser.filterArgType(flag).outTrueValue(cmdLineArgInst.extractFlagVaule(flag))
  }
}
