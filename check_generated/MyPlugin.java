package org.jenkins.ci.plugins.jobimport;

import hudson.Extension;
import hudson.model.RootAction;


import hudson.model.Run;
import jenkins.model.RunAction2;




@Extension
public class MyPlugin implements RootAction ,RunAction2 {
    
    private transient Run run; 
    
    @Override
    public void onAttached(Run<?, ?> run) {
        this.run = run; 
    }

    @Override
    public void onLoad(Run<?, ?> run) {
        this.run = run; 
    }

    public Run getRun() { 
        return run;
    }

    @Override
    public String getIconFileName() {
        return "headshot.png";
    }

    @Override
    public String getUrlName() {
        return "myplugin";
    }

    @Override
    public String getDisplayName() {
        return "My Plugin";
    } 
    
}
