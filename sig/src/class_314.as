package
{
   import flash.display.Loader;
   import flash.net.URLRequest;
   import flash.events.IOErrorEvent;
   import flash.events.Event;

   public class class_314 extends Loader
   {

      public function class_314(param1:String, param2:String, param3:Function, param4:Function = null)
      {
         super();
         this.url = param1 + "/salt?postfix=" + param2;
         this.completeHandler = param3;
         this.failHandler = param4;
         this.contentLoaderInfo.addEventListener(Event.COMPLETE,this.method_533);
         this.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR,this.method_1684);
         this.request = new URLRequest(param1);
         load(this.request);
      }

      private static var var_1767:int = 3;

      public var url:String;

      public var completeHandler:Function;

      private var failHandler:Function;

      private var request:URLRequest;

      private var var_1152:int = 0;

      public var loaded:Boolean = false;

      public var saltFunc:Function;

      private function method_1684(param1:IOErrorEvent) : void
      {
         if(this.var_1152 < var_1767)
         {
            this.var_1152++;
            this.request = new URLRequest(this.url);
            load(this.request);
         }
         else
         {
            this.loaded = false;
            this.contentLoaderInfo.removeEventListener(Event.COMPLETE,this.method_533);
            this.contentLoaderInfo.removeEventListener(IOErrorEvent.IO_ERROR,this.method_1684);
            if(this.failHandler != null)
            {
               this.failHandler(this);
            }
         }
      }

      private function method_533(param1:Event) : void
      {
         var _loc2_:Object = param1.target.content;
         this.saltFunc = _loc2_.saltFunc;
         this.loaded = true;
         this.contentLoaderInfo.removeEventListener(Event.COMPLETE,this.method_533);
         this.contentLoaderInfo.removeEventListener(IOErrorEvent.IO_ERROR,this.method_1684);
         this.completeHandler(this);
      }
   }
}