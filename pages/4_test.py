# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import inspect
import textwrap
import time
import numpy as np
from utils import show_code


url = "https://00f74ba44bebe612f16719bdd174531c42b28d2cbe-apidata.googleusercontent.com/download/storage/v1/b/for_demo_mori/o/streamlit%2Fout.mp4?jk=AFshE3UAgMFlm9F9cU4QoRIKBdtgS1MP5dv0Kr36fNzbc312Zd1Kx_pM3FJVG2XAAuTmuK1pMlEyfLKzQ-npXOsfedfh1r9U9LelCSPNO8FQZUpq0w3Bl7ntVch9iaaMVJ60I3PJz51Vv1NXiLKAOazCOJxvobCEUsJH8yJ80TXsejR3LdgIl5AXTRCVKpfA0MQzmADUzv_9FPcLfQLCRwnDwnApwLglN8Y54C8F1XxOddAaF6KXGu8P0PcfAOPpxSKZjOYK-lqnnDCZfcPnVs5hw_8kKMHHmEotPPub7Pvm4H4cm4qXNC3_iaNH22nqxQuIgrzrhFgt3pFWGWWSWwyb074U-qkC-v2iCTrm0ZWOzkOTjDedXIDX3cYDaGpDAIiygaMmbgg-ydF_TUb8qMCcBVBCUXKPB3hYmZqAqAWz1PjXrdzCXaJc4hp0f8KZzx5X6gDCgQcUdF1PdPiqSTnaWBF0YL-a0reY1az80-81C-A0QMUBdobw-I-j3tsGtZvWZtoU8ot7MRMSU0qOuxEp3j--jVWg9-VECq4X-SfAuacluNDasuDl6tnhBp0knEBgkIspITtWQJNUQxaerULV9YWFugpn1dVbxJlQPSBK5cVbPudxcvP3AlXmowlDJk8uN1bbKm-WNRe2jB1FZyuMhUA7SNz1cofRHI9CSiXKnqXuhKHP0Wrn0asSJLIPuTmBtUzQMhd_7jeNB2ZQAkocCjGcxp3kJSHwVqyCIBXcQ6vxpFZApXp7G-ucLiuJpkXiGnQLyBDxfD9DLItrfs1awSsIpNZNAOPUUYf1aETs_eMzSTdJ8hlGQx2HRcR1eIs1OKGgyLWO0c33qxEgVcPgg9koj5cMYWIccHGUeRBBO767A1nJ4qZSe9HWuvzgL7iCYx1KmX1RT18IlQUNfLN0z2Su2JPh5UaWDp_GZDy9sgN6FcI6mRR1hArgY5jAn6AHq6WWHUlDb6PyTtGiJqy9jlcUkCj7iURJnuw1frNWdziv09YP3S7IHyq6Skh_TS5LUV2i4fmipNShJDnkRG1BgzWyDnt2GoCFxyiOF5WxDaptOR_XT6QYoC-md7mqqqSpUa96TR_srHeQvIkR1Y-ySS5i7_BS1rwjRuplR60Wgm1Pdwz-id5-Ouov44_ECV-yQPEgNwSqnmdErGJgDCVo9hiTNg4&isca=1"

def vision_demo():
    #progress_bar = st.sidebar.progress(0)
    #status_text = st.sidebar.empty()
    #last_rows = np.random.randn(1, 1)
    #chart = st.line_chart(last_rows)

    #progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    #st.button("Re-run")
    st.video("https://www.youtube.com/watch?v=eWNOaEbxhd4")


st.set_page_config(page_title="ComputerVision Demo", page_icon="")
st.markdown("# ComputerVision Demo")
st.sidebar.header("ComputerVision Demo")
st.write(
    """あああ"""
)

vision_demo()

#show_code(plotting_demo)
