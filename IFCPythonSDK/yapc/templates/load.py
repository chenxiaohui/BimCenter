        if self.args.argc()<=idx+{idx}:
            log.error("Inverse links : Error during reading parameter {idx} of {name}, line %d"%common.counter)
            return False

        currentRefList={func}(self.args.argv[idx+{idx}])      
        if currentRefList:
            if currentRefList[0]==ID_UNDEF:
                log.error("Inverse links : Error during reading parameter {idx} of {name}, line %d"%common.counter)
                return False
            if currentRefList[0]!=ID_UNSET:
                for i in currentRefList:
                    self.expDataSet.getArgs(i).addInverse('{name|upper}','{attr}',self.lid)
