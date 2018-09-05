import matplotlib.pyplot as plt

def cluster_inertia(X_nmf, X_lsa, start, stop):
    inertia_lsa = [0,0]
    inertia_nmf = [0,0]

    for n_clusters in range(start, stop):
        km_nmf = KMeans(n_clusters = n_clusters)
        km_nmf.fit(X_nmf)
        msg_nmf = f"""# clusters: {n_clusters:2d}   Inertia: {km_nmf.inertia_:8.6f}"""
        inertia_nmf.append(km_nmf.inertia_)
        # print(msg_nmf)

        km_lsa = KMeans(n_clusters = n_clusters)
        km_lsa.fit(X_lsa)
        msg_lsa = f"""# clusters: {n_clusters:2d}   Inertia: {km_lsa.inertia_:8.6f}"""
        inertia_lsa.append(km_lsa.inertia_)
        # print(msg_lsa)

    f, ax = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True, figsize=(20,6))
    f.subplots_adjust(hspace=0.3)

    ax[0].set_title('NMF Kmeans Inertia')
    ax[0].plot(inertia_nmf)
    ax[0].set_xlim([start, stop])
    ax[1].set_title('LSA Kmeans Inertia')
    ax[1].plot(inertia_lsa)
    ax[1].set_xlim([start, stop])

    return inertia_nmf, inertia_lsa

def clean_dolla(data):
    data = data.fillna('$0.00')
    cleaned = [float(x.replace(",", "").strip("$")) for x in data]
    return cleaned

def plot_bar(data, figh=5, figv=3):
    plt.figure(figsize=(figh,figv))
    summary=data.value_counts()
    plt.bar(summary.index, summary)

    ax=plt.gca()
    for i, v in enumerate(summary):
        ax.text(i, v + 10, f'{v}', fontsize=12, color='b', horizontalalignment='center')
