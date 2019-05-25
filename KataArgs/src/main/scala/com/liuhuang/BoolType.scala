package main.scala.com.liuhuang

class BoolType(flag: String, default: String) extends ArgType {

  override def getFlag: String = flag
  override def getType: String = "Boolean"
  override def getDefault: String = default
  override def outTrueValue(value: String): Boolean = {
    if(value.isEmpty) return default.toBoolean
    value.toBoolean
  }
}
