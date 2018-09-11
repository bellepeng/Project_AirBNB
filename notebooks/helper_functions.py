import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Data Cleaning
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

# Topic Modeling
def display_topics(model, fit, feature_names, no_top_words, topic_names=None):
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic {a:} score: {b: 6.1f}%".format(a=ix, b=100*sum(fit[:,ix])/fit.sum()   ))
        else:
            print("\nTopic {a:} score: {b: 6.1f}%".format(a=topic_names[ix], b=100*sum(fit[:,ix])/fit.sum()   ))
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

# Unsupervised Learning
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


# Linear Modelling
def diagnostic_plot(y, pred, figsize=(10,5)):
    plt.figure(figsize=figsize)
    res = y - pred

    plt.subplot(1, 3, 1)
    plt.scatter(y, pred)
    plt.plot(np.linspace(y.min()-0.01*np.mean(y), y.max()+0.01*np.mean(y), 1000),
         np.linspace(y.min()-0.01*np.mean(y), y.max()+0.01*np.mean(y), 1000),
        color='m', linestyle='--')
    plt.title("Actual vs. Predicted", size=15)
    plt.xlabel("Actual", size=15)
    plt.ylabel("Predicted", size=15)

    plt.subplot(1, 3, 2)
    plt.scatter(pred, res)
    plt.plot(np.linspace(pred.min()-0.01*np.mean(pred), pred.max()+0.01*np.mean(pred), 1000),
             np.linspace(0, 0, 1000),
             color='m', linestyle='--')
    plt.title("Residual plot of Y-Predict", size=15)
    plt.xlabel("Prediction", size=15)
    plt.ylabel("Residuals", size=15)

    plt.subplot(1, 3, 3)
    stats.probplot(res, dist="norm", plot=plt)
    plt.xlabel("Theoretical Quantiles", size=15)
    plt.ylabel("Ordered Values", size=15)
    plt.title("Normal Q-Q plot", size=15)

# compute with R^2 formulas from the theory
def calc_Rsq(y, pred, num_feat):
    SS_Residual = sum((y-pred)**2)
    SS_Total = sum((y-np.mean(y))**2)
    r_squared = 1 - (float(SS_Residual))/SS_Total
    adjusted_r_squared = 1 - (1-r_squared)*(len(y)-1)/(len(y)-num_feat-1)
    mean_root_error = np.sqrt(np.mean((y - pred)**2))
    return ({'r_squared: ': r_squared,
             'adjusted_r_squared: ': adjusted_r_squared,
             'mean_root_error: ': mean_root_error})
