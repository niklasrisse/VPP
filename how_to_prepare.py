import pandas as pd

def separate_vulns_and_patches(df):
    
    patches = df.drop('vulnerable_func', axis=1)
    patches = patches.rename(columns={'patched_func': 'func'})
    patches["target"] = 0
    
    vulns = df.drop('patched_func', axis=1)
    vulns = vulns.rename(columns={'vulnerable_func': 'func'})
    vulns["target"] = 1
    
    fused_df = patches.append(vulns)
    fused_df = fused_df.reset_index()
    
    return fused_df

vpp_train = pd.read_json('./VulnPatchPairs-Train.json')
vpp_valid = pd.read_json('./VulnPatchPairs-Valid.json')
vpp_test = pd.read_json('./VulnPatchPairs-Test.json')

vpp_train = separate_vulns_and_patches(vpp_train)
vpp_valid = separate_vulns_and_patches(vpp_valid)
vpp_test = separate_vulns_and_patches(vpp_test)