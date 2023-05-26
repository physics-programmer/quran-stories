from gpt4_openai import GPT4OpenAI
from langchain import LLMChain
from langchain.prompts.chat import (ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate)

# Token is the __Secure-next-auth.session-token from chat.openai.com
my_session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..0qOUtAWfTDSlIXQN.HvCumJWR-q0uxSiqFz7toViXJGOD4SCJ21z68FEMHYCJOgkXJ8NJfCFZm897idgs0C-Axty6wl1H_sM7cPtlb2PUNsCwCGOIDp-rd4dkqQYEwPMY5GCLOpksBjcfHwNAvSpV-nti12MxcBNPb541jCqNNQDXV5PnMaIKwMdL4f0R2WX2-qDBQ2l13BY9ioRJc0EGSmdFJtGUEVdk_8i4D4q2i2UXcMUybu6oPXdRpCMFUputmUINQBFavTAuNwll3qob3-4EO9T4Yx6zv1ElSWaqkotldW8qZ_qQfpchD-LwOmC-gPXpz-piliySPiWh3FxY7gVvZL3X56qzqw1bWwDiNNmK4NcwF8LJqw9aFGnUWAST70fL_ydiy5YcJvGYmfA1IAnn0xc2Z3Zrd_DRcyUXKMoGoYPNeN1-cChkuAiwaPT3sIJoIOnSisyOXHQFwalnzQQHOXEBzLT9-21FKAAUZZ03N_loQGwm1cQ4cmvUvO4G-0p6OB9Y_gjvvT92bLu6L4BPu8ROO3XyH_PFV2WZhoN7JBOvGR_l1MWl_UvpGPSdr9SSpKbUzb-RkX7e-44sz2u1EsAxwfZIKzI6aLIfj3w3lVs5rF70cVM3KsAS29qOA1hXKegodCxylYmdtrR32xstyWWC1wjfoUhm1DxsnTNsCb8qJnM41ovLh05U6kLFK2A2FKOjT1UuZe9QW2WmVFoVxDuTpxVNrTP_Mda42mtMMm8GszGDijUBUz4KIY4j2bTA5HTgFLTStE7aCvRyyI-98qcXvnxoUc8xIc8pv_nRZiVtiLAr0pgGEP_WjG7MO3BCgp4j28Sg-34pzo7zlHPdO-hU98cW9fscbmU2CaatdVKWrYQK8NjB6f8vUc9ZvlvuzFVhdHVcxYeJ4t3wRNEndV2flUjYMvhKI2NaIeWvl2NHhN6uU-LNvH0AH460z_FiIHwpR6nInCp05gPdm6pTixJFN7YrGCL5yqW6QhUrqnchMfX_URHxL2lHi2WiUo_7VTlCR8siwwi_zQw0CBbx3quyPhi6EMKdlmVdh54Y3AcyLKQfcW4WQSScP8V3qMhcPtUgO6lfo5pIRssvmkMI8T4hgfQhd3wzbFPEJMgDwlvKlbRGEbL1OGovZfws1l-RojkNj0Loc2qIvKP7y-8ihQG5KvetNvNbJWxUsHeZ6e4NcxPzupTMCxS7CigBFC5oIHgzA6kC--f3eyHV3YCkPfHGtH3g2AKhEU7sebJkfM8tnEGK38aw1gxlU8JU13XXnK6FRs0CVXpA_Vx1FgNASSx2jrLoLyFPj_Ikf6zM_6RcagbWcjS52XzsXtbzaEeVIxLyWls1qw1Xc3t2oZqQHlJLAgWuOMUg4SbG8_yt2St4SKzTf8d5n3dK9mi6ayMU4JI9optLRWnYpFpMMvbH_9tzQU_efIb3CVZIHCfQbilFgKWx4th0_gDolUTcwb1DmGjPkTOxLOs-pR2HOd5OERubHBdmgxEWyYgXlNbFPZLstIMg0JmGN2fXbiAAEAsiuT6bObysPq9TMBjGsUq-I2naWWafsabnNj2DGn_kRWoZzuSP_J7z92Q8UVdrO9mRdgKWIJlqKCXjwPu9sNXIijpXDIeXLXLYkGwrTqXU7eQUBKIVJNJoQdASe4aMgwG_x-KdahYzcELpcd6OeLlJnrod-7X9WONCXS1tCnVnp1ZqHak42Kf0MRhTjQ-MZHx6g87GoKyOhk2p58MqNAMg7LisXHfRhs6TGnLixdf56J1oZjqVfavffdfqVf2ILGbyvoakGafRfKHxFOJLK_R7JtSZ4T9xIgRiXg3dHb_YITLuhBTsizoExSDE42a75vSJyhcHa9C_2UpjdTHW-f_fm7yic1vrdfn6qsLjO0pH-gsjTt_rjTilP0DsAZ5y_RE2ONLkfreEKuO-Owfz-gI67DU3Iy35tG8yvm_VMfNww236m5_mn_Um-uDJAobAkLLasX5JqeCLGz0t8ROo7BKL3hI_lGWeUZYScf1RSVhvX6b6H6sPzzs9s_rjRZJJMadEmHDIhpIQKkF7u7srZZ6XQL0Mmty8MtwuDOckbsdodNZFePLym7T9H2VP-OZnIeRqhxBZR-nGX0pCdHUBpnSQjkSF2_FQHdXO3W0X6dn5shEYQnYipVLe199UbEIhnh_yKNw6HE_CTsyqU5xuPQ9SWbaU61LpNNEOUa06ZAJcs9v7XvPTeqsH5nVJ5XUVC_oQJu9QCMO4ynciB3I7rOqD5Zt2jrRjHgl2zYYboSG84SrGFpao4P-_rxsgDW4x-YaFjXdkE7odwwM86r7HG64XbbCF305Tn6V-iZ_57ZD-TajDAP2M1PHYu7L4j8DHACIkYbnqVZP-pvDO8lvYbzqwcdSrzifC9DA_8_c4HLNoxVQzJ3QlgFLv8Ls7YIAf9c9alPqo6_J6XETIjFUHSNM6tF3zN_gnDBGRTYBcUczQyChW782lnKYp-bUUJ_7qzKHVyYX0AKWB4NdKXjQIAKD4PxQ8mYdMsdQOYEosSl1anHh4s6t_bHwLkEY29GHIA4sh3bVN3H15EYjm7U3_.GQME7gwzIijdWZ-yswgoHw'
# llm = GPT4OpenAI(token=my_session_token, headless=False, model='gpt-4')
# # GPT3.5 will answer 8, while GPT4 should be smart enough to answer 10
# response = llm('If there are 10 books in a room and I read 2, how many books are still in the room?')
# print(response)


template="You are a helpful assistant that translates english to pirate."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template("Hi")
example_ai = AIMessagePromptTemplate.from_template("Argh me mateys")
human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])

# Token is the __Secure-next-auth.session-token from chat.openai.com
llm = GPT4OpenAI(token=my_session_token)

chain = LLMChain(llm=llm, prompt=chat_prompt)
print(chain.run("My name is John and I like to eat pizza."))