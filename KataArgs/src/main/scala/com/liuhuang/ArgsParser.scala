package main.scala.com.liuhuang

case class ArgsParser(cmdLineArgs: String, schemaArgs: String) {
  val cmdLineArgsIns = CommandLineArgs(cmdLineArgs)
  val schemaParserIns = SchemaParser(schemaArgs)

  def outFlagVaule(flag: String): Any = {
    schemaParserIns.filterArgType(flag).outTrueValue(cmdLineArgsIns.extractFlagVaule(flag))
  }
}
